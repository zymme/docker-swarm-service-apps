#!/usr/local/bin/python

import pika

try:
    print("Attempting to connect to rabbitmq ...")

    credentials = pika.PlainCredentials('mydev', 'p@ssIt!')
    parameters = pika.ConnectionParameters('192.241.227.72', 5672, '/', credentials)

    connection = pika.BlockingConnection(parameters)

    channel = connection.channel()

    print("connected to broker on 192.241.227.72 ...")

    message = "{ 'message': 'my test message', 'from': 'python test sender' }"

    channel.queue_declare(queue='messaging')

    channel.basic_publish(exchange='', routing_key='messaging', body=str(message))

    print(" [x] Sent {} ".format(message))

    connection.close()

except Exception as e:
    print("ERROR {}".format(e))
