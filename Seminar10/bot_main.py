# Задача 1. Напишите бота для техподдержки. Бот должен записывать обращения пользователей в файл.
# Задача 2. Добавьте боту модуль, который позволяет считывать из файла вопрос,
# отвечать на него и отправлять ответ обратно пользователю.

import telebot
import bot_state
from common_btn import send_buttons as sb

print('Start')

token_bot = "5764995796:AAEFcUF-ZtlQthT5kx8Hodzp3zt5HKCgdmA"
bot = telebot.TeleBot(token_bot, parse_mode=None)


@bot.message_handler(commands=['start'],)
def send_welcome(message):
    curUser = message.from_user.id
    curChat = message.chat.id
    print(f'{curUser} {message.text}')

    if message.text == '/start':
        bot_state.start_question(curUser)
        bot.send_message(curChat, "Центр поддержки...")
        sb(bot, curChat, "Введите Ваш вопрос?", ['Отменить', ])


@bot.message_handler(content_types=['text'])
def send_welcome(message):
    curUser = message.from_user.id
    curChat = message.chat.id
    print(message.text)

    if message.text == 'Отменить':
        bot.send_message(curChat, 'Если появятся вопросы. Наберите /start')
        bot_state.done_question(curUser)
        return

    if message.text == 'Ответ получен':
        bot.send_message(curChat, 'Рад был помочь...')
        bot.send_message(curChat, 'Если появятся вопросы. Наберите /start')
        bot_state.done_question(curUser)
        return

    if message.text == 'Статус':
        cs = bot_state.get_current_state(curUser)
        if cs == 'wait':
            sb(bot, curChat, "Ведите Ваш вопрос?", ["Статус", "Отменить"])
        if cs == 'process':
            sb(bot, curChat, "Ваш запрос обрабатывается...",
               ["Статус", "Отменить"])
        if cs == 'answer':
            asw = bot_state.get_answer(curUser)
            sb(bot, curChat, f"Ответ: {asw}", ["Статус", "Ответ получен"])
        if cs == 'done':
            bot.send_message(curChat, 'Активных вопросов нет.')
            sb(bot, curChat,
               'Если появятся вопросы. Наберите /start', ["Статус"])
        return

    if bot_state.get_current_state(curUser) == 'wait':
        bot_state.set_question(curUser, message.text)
        sb(bot, curChat, "Ваш запрос обрабатывается...",
           ["Статус", "Отменить"])


bot.infinity_polling()
