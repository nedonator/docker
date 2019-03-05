import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq', 5672))
channel = connection.channel()
channel.queue_declare(queue = 'my_queue')

def callback(channel, method, properties, body):
  print(body)

channel.basic_consume(callback, queue = 'my_queue', no_ack = True)
channel.start_consuming()
