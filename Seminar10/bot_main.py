# Задача 1. Напишите бота для техподдержки. Бот должен записывать обращения пользователей в файл.
# Задача 2. Добавьте боту модуль, который позволяет считывать из файла вопрос,
# отвечать на него и отправлять ответ обратно пользователю.

from telebot import types
import telebot
import bot_state


print('Start')

token_bot = "5764995796:AAEFcUF-ZtlQthT5kx8Hodzp3zt5HKCgdmA"
bot = telebot.TeleBot(token_bot, parse_mode=None)

states = {'wait': "Введите Ваш вопрос",
          'process': "Ваш запрос обрабатывается",
          'answer': "Ответ",
          'done': "Вопрос закрыт"}


@bot.message_handler(commands=['start'],)
def send_welcome(message):
    curUser = message.from_user.id
    curChat = message.chat.id
    print(f'{curUser} {message.text}')

    if message.text == '/start':
        bot_state.start_question(curUser)
        bot.send_message(curChat, "Центр поддержки...")
        send_buttons(curChat, "Введите Ваш вопрос?", ['Отменить', ])


def send_buttons(curChat: int, msg: str, btn_list: list):
    markup = types.ReplyKeyboardMarkup(
        resize_keyboard=True, one_time_keyboard=True)

    markup.row(*[types.KeyboardButton(x) for x in btn_list])
    bot.send_message(curChat, msg, reply_markup=markup)


@bot.message_handler(content_types=['text'])
def send_welcome(message):
    curUser = message.from_user.id
    curChat = message.chat.id
    print(message.text)

    if message.text == 'Отменить':
        bot.send_message(curChat, 'Если появятся вопросы. Наберите /start')
        bot_state.done_question(curUser)
        return

    if message.text == 'Статус':
        cs=bot_state.get_current_state(curUser)
        if cs=='wait':
            send_buttons(curChat, "Ведите Ваш вопрос?",["Статус", "Отменить"])
        if cs=='process':
            send_buttons(curChat, "Ваш запрос обрабатывается...",["Статус", "Отменить"])
        if cs=='answer':
            asw=bot_state.get_answer(curUser)
            send_buttons(curChat, f"Ответ: {asw}",["Статус", "Отменить"])
        if cs=='done':
            bot.send_message(curChat, 'Активных вопросов нет.')
            send_buttons(curChat, 'Если появятся вопросы. Наберите /start',["Статус"])
        return

    if bot_state.get_current_state(curUser) == 'wait':
        bot_state.set_question(curUser, message.text)
        send_buttons(curChat, "Ваш запрос обрабатывается...",
                     ["Статус", "Отменить"])

    # if bot_state.get_current_state(curUser) == 'process':
    #     if message.text == 'Статус':
    #         bot.send_message(curChat, "Ваш вопрос обрабатывается...")
    #         bot.send_message(curChat, bot_state.questino(curUser))
    #         markup = types.ReplyKeyboardMarkup()
    #         itembtn_question = types.KeyboardButton('Статус')
    #         itembtn_allright = types.KeyboardButton('Отменить')
    #         markup.row(itembtn_question, itembtn_allright)
    #         bot.send_message(curChat, "?", markup)

    #     if message.text == 'Отменить':
    #         bot_state.start_question()


bot.infinity_polling()
