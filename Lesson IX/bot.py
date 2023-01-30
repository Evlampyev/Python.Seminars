# token1 = "5916882745:AAHDomrnWWXirqjByn6-XiztHz9nDXolK1Q"
from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from random import randint

token1 = "5916882745:AAHDomrnWWXirqjByn6-XiztHz9nDXolK1Q"

bot = Bot(token="5916882745:AAHDomrnWWXirqjByn6-XiztHz9nDXolK1Q")
updater = Updater(token1)
dispatcher = updater.dispatcher


def start(update, contex):
    contex.bot.send_message(update.effective_chat.id, "Hello")


def rand(update, contex):
    contex.bot.send_message(update.effective_chat.id, f'{randint(1, 100)}')


def default(updater, contex):
    contex.bot.send_message(updater.effective_chat.id, "Я не знаю таких команд")


print("Server start")
start_handler = CommandHandler('start', start)
random_handler = CommandHandler('random', rand)
default_handler = MessageHandler(Filters.command, default)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(random_handler)
dispatcher.add_handler(default_handler)

updater.start_polling()
updater.idle()
