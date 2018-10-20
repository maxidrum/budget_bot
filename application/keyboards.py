from telegram import InlineKeyboardButton


main_keyboard = [[InlineKeyboardButton('Расход', callback_data='expense'),
                  InlineKeyboardButton('Доход', callback_data='income')],
                 [InlineKeyboardButton('Статистика', callback_data='blance')]]

group_keyboard = [[InlineKeyboardButton('еда', callback_data='g_1')],
                  [InlineKeyboardButton('комуналка', callback_data='g_2')],
                  [InlineKeyboardButton('кафе и рестораны', callback_data='g_3')],
                  [InlineKeyboardButton('транспорт', callback_data='g_4')],
                  [InlineKeyboardButton('меню', callback_data='main')]
                  ]
