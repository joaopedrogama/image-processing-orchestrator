import json

def consume_from_videos_processed(channel, method, properties, body):
    from videos.models import Video

    print(" [x] Received %r from channel %r" % (body, channel))

    body_json = json.loads(body.decode('utf-8'))

    print("Decoded body:", body_json)

    try:
        Video.objects.create(
            name=body_json['name'],
            video_file=body_json.get('video_file', None),
        )
    except Exception as e:
        print(e)
