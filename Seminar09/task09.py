# Задача 1. Добавьте telegram-боту возможность вычислять выражения: 1 + 4 * 2 -> 9

# Задача 2. Добавьте в бота игру «Угадай числа». Бот загадывает число от 1 до 1000.
# Когда игрок угадывает его, бот выводит количество сделанных ходов.

import time
import requests
import telebot


token_bot = "5949396844:AAF0WFXRL1reMxkUKDkUlKGTLfxqwu-FzCM"
bot = telebot.TeleBot(token_bot, parse_mode=None)


@bot.message_handler(commands=['start', 'help', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")


# @bot.message_handler(func=lambda m: True)
# def echo_all(message):
#     data = open('user_message.txt', 'a+', encoding='utf-8')
#     data.writelines(str(message.from_user.id) + ' ' + message.text + '\n')
#     data.close()


@bot.message_handler(content_types=["text"])
def hello_user(message):
    if 'привет' in message.text:
        bot.reply_to(message, 'привет, ' + message.from_user.first_name)
    elif message.text == 'играть':
        bot.reply_to(message, 'хочешь поиграть?')
    elif message.text == 'погода':
        r = requests.get('https://wttr.in/?0T')
        bot.reply_to(message, r.text)
    elif message.text == 'котик':
        r = f'https://cataas.com/cat?t=${time.time()}'
        bot.send_photo(message.chat.id, r)
    elif message.text == 'файл':
        data = open('user_message.txt', encoding='utf-8')
        bot.send_document(message.chat.id, data)
        data.close()


bot.infinity_polling()
