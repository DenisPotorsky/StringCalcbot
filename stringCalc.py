import telebot

import calculator

api_token = "8035819275:AAHhFOuCk8QwNKC4Bd4u94UQHuWTx-a-RwI"
bot = telebot.TeleBot(api_token)


@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/start':
        bot.send_message(message.from_user.id, 'Привет! Введите общий диаметр струны')
        bot.register_next_step_handler(message, get_general)


def get_general(message):
    global general
    general = float(message.text)

    bot.send_message(message.from_user.id, 'Введите керн')
    bot.register_next_step_handler(message, get_kern)


def get_kern(message):
    global kern
    kern = float(message.text)

    bot.send_message(message.from_user.id, 'Введите длину навивки')
    bot.register_next_step_handler(message, get_lengthCooper)


def get_lengthCooper(message):
    global len
    len = float(message.text)

    bot.send_message(message.from_user.id, 'Введите тип струны: 1 или 2')
    bot.register_next_step_handler(message, calculate)


def calculate(message):
    global type_of_string
    type_of_string = message.text
    if type_of_string == '1':
        cooper = round(calculator.cooperDiamm(general, kern), 3)
        lengthCooper = round(calculator.lengthCoop(kern, cooper, len), 3)
        bot.send_message(message.from_user.id, f'Диаметр меди {cooper}, длина проволоки {lengthCooper}')
    else:
        coopFirst = round(calculator.cooperF(general, kern), 3)
        coopSecond = round(calculator.cooperS(kern, general), 3)
        lenCoopFirst = round(calculator.lengthCooperPrim(kern, len, coopFirst), 3)
        lenCoopSec = round(calculator.lengthCooperSec(kern, len, coopFirst, coopSecond), 3)
        bot.send_message(message.from_user.id,
                         f'Диаметр меди первичной навивки {coopFirst}, диаметр меди вторичной навивки {coopSecond}, '
                         f'длина проволоки первичной навивки {lenCoopFirst}, длина проволоки вториной навивки {lenCoopSec}')


bot.polling(none_stop=True)
