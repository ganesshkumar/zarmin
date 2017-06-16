import pika, os, urlparse, logging
logging.basicConfig()

url = os.environ['CLOUDAMQP_URL']
params = pika.URLParameters(url)
params.socket_timeout = 5

connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue='notify')

channel.basic_publish(exchange='', routing_key='notify', body='One..Two..Three')
connection.close()
