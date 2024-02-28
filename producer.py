import pika
import json
from constants import RABBITMQ_URL

params = pika.URLParameters(RABBITMQ_URL)

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):

    properties = pika.BasicProperties(method)

    channel.basic_publish(exchange='', routing_key='order', body=json.dumps(body), properties=properties)

