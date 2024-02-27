import pika
from constants import RABBITMQ_URL

params = pika.URLParameters(RABBITMQ_URL)

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='owner')

def callback(ch, method, properties, body):

    print('Received in owner')

    print(body)

channel.basic_consume(queue='owner', on_message_callback=callback)

print('Started consuming')

channel.start_consuming()

channel.close()