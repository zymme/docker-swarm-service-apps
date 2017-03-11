#!/usr/local/bin/python

import pika
import json
from pymongo import MongoClient

def save_data(message):
    print("Save Data to mongo db: {}".format(message))

    strs = str(message)
    strs = strs.replace("'",'"')
    print ("strs = : {}".format(strs))

    jsonobj = strs.replace('u"', '"')
    json_data = json.loads(jsonobj)

    client = MongoClient("mongodb://192.241.227.72:27017")
    # use IP of main container - but ideally use --net-alias for the docker network

    db = client.mydb

    print("Attempting to insert mongo document ...")

    result = db.messaging.insert_one(json_data)

    print ("Result of insert is : {} ".format(result.inserted_id))


print("Attempting to connect to the rabbitmq remote (192.241.227.72) broker ...")

try:

    credentials = pika.PlainCredentials('mydev', 'p@ssIt!')
    parameters = pika.ConnectionParameters('192.241.227.72', 5672, '/', credentials)

    connection = pika.BlockingConnection(parameters)

    channel = connection.channel()

    print("Connected to broker ...")

    channel.queue_declare(queue='messaging')


    def callback(ch, method, properties, body):

        print(" [x] Received %r " % body)
        save_data(body)


    channel.basic_consume(callback, queue='messaging', no_ack=True)


    print(' [x] Waiting for messages. To exit press Ctrl+C')

    channel.start_consuming()

except Exception as e:
    print("ERROR in receiver: {}".format(e))
