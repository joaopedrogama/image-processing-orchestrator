from datetime import datetime
from videos.models import Video
from django.db.models import Q
from ninja import FilterSchema, Query, Schema
from ninja_extra import ControllerBase, api_controller, route
from ninja_extra.pagination import PageNumberPaginationExtra, PaginatedResponseSchema, paginate
from pydantic import types


@api_controller('/videos', tags=['Videos'])
class VideoController(ControllerBase):

    class VideoRetrieveSchema(Schema):
        id: types.UUID
        name: str
        video_file: str
        created_at: str
        updated_at: str

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
