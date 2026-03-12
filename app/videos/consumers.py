import json


def consume_from_videos_processed(channel, method, properties, body):
    from videos.models import Video

    print(" [x] Received %r from channel %r" % (body, channel))

    body_json = json.loads(body.decode("utf-8"))

    print("Decoded body:", body_json)

    try:
        video_to_update = Video.objects.get(id=body_json["video_id"])
        video_to_update.zip_video_file=body_json.get("zip_url", None)
        video_to_update.save()
    except Exception as e:
        print(e)
