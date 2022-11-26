import types
import telebot
from telebot import types


def send_buttons(bot: telebot.TeleBot, curChat: int, msg: str, btn_list: list):
    markup = types.ReplyKeyboardMarkup(
        resize_keyboard=True, one_time_keyboard=True)

    markup.row(*[types.KeyboardButton(x) for x in btn_list])
    bot.send_message(curChat, msg, reply_markup=markup)
