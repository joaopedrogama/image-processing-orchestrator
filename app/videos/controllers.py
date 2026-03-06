import pika
import json
from datetime import datetime
from videos.models import Video
from django.db.models import Q
from ninja import FilterSchema, Query, Schema, UploadedFile, File, Form
from ninja_extra import ControllerBase, api_controller, route
from ninja_extra.pagination import PageNumberPaginationExtra, PaginatedResponseSchema, paginate
from pydantic import types


@api_controller('/videos', tags=['Videos'])
class VideoController(ControllerBase):

    class VideoRetrieveSchema(Schema):
        id: types.UUID
        name: str
        video_file: str
        created_at: datetime
        updated_at: datetime

    class VideoCreateSchema(Schema):
        name: str

    class VideoFilterSchema(FilterSchema):
        name: str | None = None
        created_at: datetime | None = None

        def filter_name(self, value: str | None) -> Q:
            return Q(name__icontains=value)

    @route.get('/', url_name='videos-list', response=PaginatedResponseSchema[VideoRetrieveSchema])
    @paginate(PageNumberPaginationExtra)
    def list_videos(self, filters: VideoFilterSchema = Query(...)):
        expressions = filters.get_filter_expression()
        return Video.objects.filter(expressions)


    @route.post('/', url_name='videos-create', response=VideoRetrieveSchema)
    def create_video(self, request, form: Form[VideoCreateSchema], video_file: File[UploadedFile]):
        video = Video.objects.create(
            name=form.name,
            video_file=video_file,
        )

        try:

            connection = pika.BlockingConnection(
                    pika.ConnectionParameters(
                        host='rabbitmq',
                        credentials=pika.PlainCredentials('admin', 'admin'), # TODO - add to main.py and .env
                    )
                )
            channel = connection.channel()

            body = json.dumps({
                'name': video.name,
                'video_file': video.video_file.name,
            })

            channel.basic_publish(
                exchange='',
                routing_key='video_to_process',
                body=body,
                properties=pika.BasicProperties(
                    content_type='application/json',
                    delivery_mode=1,
                ),
            )

            connection.close()
        except Exception as e:
            print(e)

        return video
