import telebot
from telebot import types
from token_id import token 

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])

def start(message):
    chat_id= message.chat.id
    murkup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard =True)
    btn1 =types.KeyboardButton('статистика')
    btn2 = types.KeyboardButton('пользователи')
    murkup.add(btn1, btn2)
    bot.send_message(chat_id, text='Hello', reply_markup=murkup)

@bot.message_handler(commands=['help'])
def help(message):
    chat_id = message.chat.id
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton('Скорая помошь', callback_data='1')
    btn2 = types.InlineKeyboardButton('Палиция', callback_data='2')
    btn3 = types.InlineKeyboardButton('Пожарные', callback_data='3')
    keyboard.add(btn1, btn2, btn3)
    bot.send_message(chat_id, text='this is help', reply_markup=keyboard)

@bot.callback_query_handler(func=lambda c: True)
def inline_(c):
    if c.data == '1':
        bot.send_message(c.message.chat.id, text='123123124')
    if c.data == '2':
        new_keyboard = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton('група захвата', callback_data='group_of_sam')
        btn2 = types.InlineKeyboardButton('гбр', callback_data='03')
        btn3 = types.InlineKeyboardButton('снайперы', callback_data='03')
        btn4 = types.InlineKeyboardButton('Back', callback_data='back')
        new_keyboard.add(btn1, btn2, btn3, btn4)
        bot.edit_message_text('кого вызвать', c.message.chat.id, c.message.message_id, reply_markup=new_keyboard)
    if c.data =='back':
        chat_id = c.message.chat.id
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton('Скорая помошь', callback_data='1')
        btn2 = types.InlineKeyboardButton('Палиция', callback_data='2')
        btn3 = types.InlineKeyboardButton('Пожарные', callback_data='3')
        keyboard.add(btn1, btn2, btn3)
        bot.edit_message_text('вы вернулись назад',chat_id, c.message.message_id, reply_markup=keyboard)

@bot.message_handler(content_types=['text'])
def bla_bla(message):
    chat_id =message.chat.id
    if message.text == 'Hello':
        bot.reply_to(message, text='Hello Hiro')
    if message.text == 'Dog':
        bot.send_message(chat_id, text='gaf gaf')

bot.polling()