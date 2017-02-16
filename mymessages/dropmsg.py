
import pika



def drop_message(message):
    print ("Message dropped!")
    print (message)

    try:
        print("Attempting to connect to rabbitmq ...")

        connection = pika.BlockingConnection(pika.ConnectionParameters(
                   'localhost'))

        channel = connection.channel()

        print("connected to broker on localhost ...")

        channel.queue_declare(queue='messaging')

        channel.basic_publish(exchange='', routing_key='messaging', body=str(message))

        print(" [x] Sent {} ".format(message))

        connection.close()

    except Exception as e:
        print("ERROR {}".format(e))
