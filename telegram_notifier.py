import os, telegram

bot = telegram.Bot(token=os.environ['TELEGRAM_BOT_TOKEN'])

def notify(chat_id, message):
    global bot
    bot.send_message(chat_id=chat_id, text=message)
