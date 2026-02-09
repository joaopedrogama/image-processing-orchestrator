import pika
from django.apps import AppConfig
from videos.consumers import process_video

class VideosConfig(AppConfig):
    name = 'videos'

    def ready(self):
        # Establish connection to RabbitMQ
        connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
        channel = connection.channel()

        # Declare the queue
        channel.queue_declare(queue='video_processing')

        # Start consuming messages from the queue
        channel.basic_consume(queue='video_processing', on_message_callback=process_video, auto_ack=True)

        print('Waiting for messages. To exit press CTRL+C')
        channel.start_consuming()
