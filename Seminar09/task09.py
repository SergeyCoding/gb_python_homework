# Задача 1. Добавьте telegram-боту возможность вычислять выражения: 1 + 4 * 2 -> 9

# Задача 2. Добавьте в бота игру «Угадай числа». Бот загадывает число от 1 до 1000.
# Когда игрок угадывает его, бот выводит количество сделанных ходов.

from telebot import types
import telebot
import controller

print('Start')

token_bot = ""
bot = telebot.TeleBot(token_bot, parse_mode=None)


@bot.callback_query_handler(func=lambda call: True)
def test_callback(call):
    print(f'call: {call}')


@bot.message_handler(commands=['start', 'game', 'calc'],)
def send_welcome(message):
    print(message.text)
    if message.text == '/start':
        controller.change_state('dialog')
        bot.send_message(message.chat.id, "3")
        bot.send_message(message.chat.id, "2")
        bot.send_message(message.chat.id, "1")
        bot.send_message(message.chat.id, "...")
        bot.send_message(message.chat.id, "Бот запущен...")
        bot.send_message(message.chat.id, "Наберите /game или /calc")
    elif message.text == '/calc':
        controller.  change_state('calc')
        bot.send_message(message.chat.id, "Калькулятор")
        bot.send_message(message.chat.id, "Введите математическое выражение: ")
    elif message.text == '/game':
        controller. change_state('game')
        bot.send_message(message.chat.id, "Угадай число")
        txt = "Я задумал число от 1 до 1000, попробуй его угадать:"
        bot.send_message(message.chat.id, txt)


@bot.message_handler(content_types=['text'])
def send_welcome(message):
    print(message.text)
    msg = controller.inProcess(message.text)
    if len(msg) > 0:
        bot.send_message(message.chat.id, msg[0])


bot.infinity_polling()
