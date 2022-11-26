import common
import telebot
from common_btn import send_buttons as sb

print('Служба поддержки \n')

token_bot = "5764995796:AAEFcUF-ZtlQthT5kx8Hodzp3zt5HKCgdmA"
bot = telebot.TeleBot(token_bot, parse_mode=None)

while True:
    id, question = common.get_active_question()

    if question == '':
        print('Вопросов нет')
        exit()

    print(question)
    answer = input("> ")

    common.create_answer(id, answer)
    common.set_state(id, 'answer')
    sb(bot, id, f"Ответ: {answer}", ["Статус", "Ответ получен"])
