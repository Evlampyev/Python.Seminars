from telegram import Bot, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler

bot = Bot(token='5916882745:AAHDomrnWWXirqjByn6-XiztHz9nDXolK1Q')
updater = Updater(token='5916882745:AAHDomrnWWXirqjByn6-XiztHz9nDXolK1Q')
dispatcher = updater.dispatcher

A = 0
B = 1


def start(update, context):
    context.bot.send_message(update.effective_chat.id, 'Привет\n Как твои дела?')
    return A


def howareyou(update, context):
    text = update.message.text
    if 'хор' in text.lower():
        context.bot.send_message(update.effective_chat.id, 'Я рад, что у тебя все хорошо')
    else:
        context.bot.send_message(update.effective_chat.id, 'Не грусти, все будет отлично')
    context.bot.send_message(update.effective_chat.id, 'Как погода?')
    return B


def weather(update, context):
    text = update.message.text
    context.bot.send_message(update.effective_chat.id, 'Ну ок, у меня тоже сегодня хорошая погода')

    return ConversationHandler.END


def cancel(update, context):
    context.bot.send_message(update.effective_chat.id, 'Прощай!!!')


start_handler = CommandHandler('start', start)
howareyou_handler = MessageHandler(Filters.text, howareyou)
weather_handler = MessageHandler(Filters.text, weather)
cancel_handler = CommandHandler('cancel', cancel)

conv_handler = ConversationHandler(entry_points=[start_handler],
                                   states={A: [howareyou_handler],
                                           B: [weather_handler]},
                                   fallbacks=[cancel_handler])
dispatcher.add_handler(conv_handler)

updater.start_polling()
updater.idle()
