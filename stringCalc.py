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

user_data = {}


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет! Пожалуйста, введите общий диаметр:')
    # Сохраняем состояние ожидания числа
    user_data[message.chat.id] = {"step": "waiting_for_name"}


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    chat_id = message.chat.id

    if chat_id in user_data:
        step = user_data[chat_id]["step"]

        if step == "waiting_for_name":
            general = message.text
            bot.send_message(chat_id, f'Спасибо, {general}! Теперь введите диаметр стали:')
            user_data[chat_id]["general"] = general
            user_data[chat_id]["step"] = "waiting_for_number"

        elif step == "waiting_for_number":
            kern = message.text
            user_data[chat_id]["kern"] = kern
            bot.send_message(chat_id, f'Вы ввели общий диаметр: {user_data[chat_id]["general"]} и диаметр стали:'
                                      f' {kern}')
            # Завершаем разговор, очищаем данные
            print(user_data[chat_id])

    else:
        bot.send_message(chat_id, 'Я не понимаю. Пожалуйста, начните с /start.')
# @bot.message_handler(commands=['start'])
# def getMessage(message):
#     bot.send_message(message.from_user.id,
#                      "Привет!", reply_markup=keyboard)
#
# @bot.message_handler(content_types=['text'])
# def get_mes(msg):
#     if msg.text == 'Расчет струны с одинарной навивкой':
#         calculate_1(msg)
#     elif msg.text == 'Расчет струны с двойной навивкой':
#         calculate(msg)
#
# def calculate_1(msg):
#     bot.send_message('Введите общий диаметр')
#     general = msg.text
#     bot.send_message('Введите диаметр стали')
#     kern = msg.text
#     calculator.
#     bot.send_message('результаты')

bot.polling(none_stop=True)
