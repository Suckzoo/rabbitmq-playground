import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello')
# routing_key parameter means queue's name declared before.
channel.basic_publish(exchange='',
                      routing_key='hello',  
                      body='Hello, world!')
print 'sent hello message to queue'


