import pika
from django.apps import AppConfig
from videos.consumers import download_zip
import threading

class VideosConfig(AppConfig):
    name = 'videos'

    def ready(self):
        # Define a function to run the RabbitMQ consumer
        def start_consumer():
            # Establish connection to RabbitMQ
            connection = pika.BlockingConnection(
                pika.ConnectionParameters(
                    host='rabbitmq',
                    credentials=pika.PlainCredentials('admin', 'admin'), # TODO - add to main.py and .env
                )
            )
            channel = connection.channel()

            # Declare the queues
            channel.queue_declare(queue='video_to_process', durable=True)
            channel.queue_declare(queue='videos_processed', durable=True)

            # Start consuming messages from the queue
            channel.basic_consume(queue='videos_processed', on_message_callback=download_zip, auto_ack=True)

            print('Waiting for messages. To exit press CTRL+C')
            channel.start_consuming()

        # Run the consumer in a separate thread
        consumer_thread = threading.Thread(target=start_consumer, daemon=True)
        consumer_thread.start()
