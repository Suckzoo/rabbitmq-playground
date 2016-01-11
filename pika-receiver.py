import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
# you need callback to work with sent messages.
def callback(ch, method, properties, body):
    print 'Received: ' + body
# queue_declare is idempotent: call as many time as you want!
# result is always same: only one queue will be there for you.
channel.queue_declare(queue='hello')
# routing_key parameter means queue's name declared before.
channel.basic_consume(callback,
                      routing_key='hello',  
                      no_ack=True)
print 'Start consuming...(Press ^C to stop)'
channel.start_consuming()
