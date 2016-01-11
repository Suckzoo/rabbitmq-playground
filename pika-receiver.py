import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
# you need callback to work with sent messages.
def callback(ch, method, properties, body):
    print 'Received: ' + body
# queue_declare is idempotent: call as many time as you want!
# result is always same: only one queue will be there for you.
channel.queue_declare(queue='hello')
# receiver uses queue parameter instead of routing_key.
channel.basic_consume(callback,
                      queue='hello',  
                      no_ack=True)
print 'Start consuming...(Press ^C to stop)'
channel.start_consuming()
