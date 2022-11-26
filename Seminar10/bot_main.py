# Задача 1. Напишите бота для техподдержки. Бот должен записывать обращения пользователей в файл.
# Задача 2. Добавьте боту модуль, который позволяет считывать из файла вопрос,
# отвечать на него и отправлять ответ обратно пользователю.

from telebot import types
import telebot
import common
import bot_state


print('Start')

token_bot = "5764995796:AAEFcUF-ZtlQthT5kx8Hodzp3zt5HKCgdmA"
bot = telebot.TeleBot(token_bot, parse_mode=None)


# @bot.callback_query_handler(func=lambda call: True)
# def test_callback(call):
#     print(f'call: {call}')

states = {1: "Введите Ваш вопрос",
          2: "Ваш запрос обрабатывается",
          3: "Ответ",
          0: "Вопрос закрыт"}


@bot.message_handler(commands=['start', 'game', 'calc'],)
def send_welcome(message):
    # for k, v in message.__dict__.items():
    #     print(f'{k}: {v}')
    print(message.json)
    curUser = message.from_user.id
    curChat = message.chat.id
    print(f'{curUser} message.text')

    if message.text == '/start':
        bot.send_message(curChat, "Центр поддержки...")
        if bot_state.get_current_state(curUser) == 2:
            bot.send_message(curChat, "Ваш вопрос обрабатывается...")
            bot.send_message(curChat, bot_state.questino(curUser))
            markup = types.ReplyKeyboardMarkup()
            itembtn_allright = types.KeyboardButton('Статус')
            itembtn_allright = types.KeyboardButton('Отменить')
            markup.row(itembtn_question, itembtn_allright)
            bot.send_message(curChat, "?", markup)
        else:
            bot.send_message(message.chat.id, "Введите Ваш вопрос?")
    elif message.text == '/calc':
        common.init_data()
    else:
        markup = types.ReplyKeyboardMarkup()
        itembtn_question = types.KeyboardButton('Нужна помощь')
        itembtn_allright = types.KeyboardButton('Вопрос решён')
        markup.row(itembtn_question, itembtn_allright)
        bot.send_message(message.chat.id, "", markup)


@bot.message_handler(content_types=['text'])
def send_welcome(message):
    print(message.text)
    # msg = controller.inProcess(message.text)
    # if len(msg) > 0:
    #     bot.send_message(message.chat.id, msg[0])


bot.infinity_polling()
