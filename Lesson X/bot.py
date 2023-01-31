from telegram import Bot, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler, CallbackContext, \
    CallbackQueryHandler
from Show import init_pole, calculation_of_winnings, output_board

bot = Bot(token='5916882745:AAHDomrnWWXirqjByn6-XiztHz9nDXolK1Q')
updater = Updater(token='5916882745:AAHDomrnWWXirqjByn6-XiztHz9nDXolK1Q')
dispatcher = updater.dispatcher

A = 0
B = 1
many = 0
win = 1


def start(update, context):
    context.bot.send_message(update.effective_chat.id, "Привет\n Ваша ставка?")


def paint_pole(update, context):
    global many
    many = int(update.message.text)
    lst = init_pole()
    text = output_board(lst)
    context.bot.send_message(update.effective_chat.id, text)
    global win
    win = calculation_of_winnings(lst)
    many = str(win * many)
    context.bot.send_message(update.effective_chat.id, f'Ваш выигрыш: {many} рупий')
    context.bot.send_message(update.effective_chat.id, 'Ваша ставка')


start_handler = CommandHandler('start', start)
paint_pole_handler = MessageHandler(Filters.text, paint_pole)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(paint_pole_handler)

updater.start_polling()
updater.idle()
