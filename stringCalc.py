from wsgiref import headers

import telebot

import requests
from urllib3.util import url

import json

from calculator import cooperDiam

api_token = "8035819275:AAGAPvklVOpUOgKBvs94Wf4cvj_iYEurinI"
bot = telebot.TeleBot(api_token)

bot = telebot.TeleBot(api_token)

keyboard = telebot.types.InlineKeyboardMarkup()
keyboard.row(telebot.types.InlineKeyboardButton('Расчет струны с однинарной навивкой', callback_data=' '))
keyboard.row(telebot.types.InlineKeyboardButton('Расчет струны с двойной навивкой', callback_data=' '))


@bot.message_handler(commands=['start'])
def getMessage(message):
    bot.send_message(message.from_user.id,
                     "Привет!", reply_markup=keyboard)

@bot.message_handler(content_types=['text'])
def get_mes(msg):
    if msg.text == 'Расчет струны с одинарной навивкой':
        calculate_1(msg)
    elif msg.text == 'Расчет струны с двойной навивкой':
        calculate(msg)

def calculate_1(msg):
    bot.send_message('Введите общий диаметр')
    general = msg.text
    bot.send_message('Введите диаметр стали')
    kern = msg.text
    calculator.
    bot.send_message('результаты')

bot.polling(none_stop=True)
