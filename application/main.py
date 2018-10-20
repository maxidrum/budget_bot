import logging

from telegram.ext import Updater
from telegram.ext import CallbackQueryHandler, CommandHandler
from telegram import Bot, InlineKeyboardMarkup

from application import keyboards


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


MAIN_MESSAGE = 'Меню: '


def start(bot, update):
    update.message.reply_text(MAIN_MESSAGE,
                              reply_markup=main_menu_keyboard())


def main_menu(bot, update):
    query = update.callback_query
    logging.info(update)
    bot.edit_message_text(chat_id=query.message.chat_id,
                          message_id=query.message.message_id,
                          text=MAIN_MESSAGE,
                          reply_markup=main_menu_keyboard())


def expense(bot, update):
    query = update.callback_query
    bot.edit_message_text(chat_id=query.message.chat_id,
                          message_id=query.message.message_id,
                          text=MAIN_MESSAGE,
                          reply_markup=expense_groups_keyboard())


def income(bot, update):
    query = update.callback_query
    bot.edit_message_text(chat_id=query.message.chat_id,
                          message_id=query.message.message_id,
                          text=MAIN_MESSAGE,
                          reply_markup=()) # keyboard


def main_menu_keyboard():
    return InlineKeyboardMarkup(keyboards.main_keyboard)


def expense_groups_keyboard():
    return InlineKeyboardMarkup(keyboards.group_keyboard)


def g_1(bot, update):
    query = update.callback_query
    bot.send_message(chat_id=query.message.chat_id, text='None')


bot = Bot(token)
updater = Updater(token)
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CallbackQueryHandler(main_menu, pattern='main'))
dispatcher.add_handler(CallbackQueryHandler(expense, pattern='expense'))
dispatcher.add_handler(CallbackQueryHandler(income, pattern='income'))
dispatcher.add_handler(CallbackQueryHandler(g_1, pattern='g_1'))

updater.start_polling()