
import pika



def drop_message(message):
    print ("Message dropped!")
    print (message)

    try:
        print("Attempting to connect to rabbitmq ...")

        # connection = pika.BlockingConnection(pika.ConnectionParameters(
        #            'localhost'))

        credentials = pika.PlainCredentials('mydev', 'p@ssIt')
        # parameters = pika.ConnectionParameters('192.241.227.72', 5672, '/', credentials)
        parameters = pika.ConnectionParameters('zedsmongodb', 5672, '/', credentials)

        connection = pika.BlockingConnection(parameters)

        channel = connection.channel()

        print("connected to broker ...")

        channel.queue_declare(queue='messaging')

        channel.basic_publish(exchange='', routing_key='messaging', body=str(message))

        print(" [x] Sent {} ".format(message))

        connection.close()

    except Exception as e:
        print("ERROR {}".format(e))
