import pika, os, urlparse, logging
from telegram_notifier import notify

logging.basicConfig()
logger = logging.getLogger('zarmin')
CLIENT_ID = os.environ['MY_CLIENT_ID']

def callback(ch, method, properties, body):
    global CLIENT_ID
    notify(CLIENT_ID, body)

# Params
url = os.environ['CLOUDAMQP_URL']
params = pika.URLParameters(url)
params.socket_timeout = 5
# Create a connection
connection = pika.BlockingConnection(params)
channel = connection.channel()
# Create queue if it doesn't exist
channel.queue_declare(queue='telegram')
# Listen to the queue
logger.info('Listening to the queue')
channel.basic_consume(callback, queue='notify', no_ack=True)
channel.start_consuming()
# Close the connection
connection.close()
