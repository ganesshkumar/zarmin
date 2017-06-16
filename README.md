# zarmin
> bridges CloudAMQP with telegram

## Required environmental variables
* CLOUDAMQP_URL
* TELEGRAM_BOT_TOKEN
* MY_CLIENT_ID

## Contents
* `app.py` listens on a CloudAMQP queue and pushes any incoming messages to telegram client.
* `test_publisher.py` - sample code to publish a message into CloudAMQP queue.
