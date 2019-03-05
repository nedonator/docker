import numpy as np
import pika
import numpy.random
import time

connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq', 5672))
channel = connection.channel()
channel.queue_declare(queue = 'my_queue')
while(True):
  time.sleep(np.random.rand())
  channel.basic_publish(exchange = '', routing_key = 'my_queue', body = str(np.random.randint(100)))
