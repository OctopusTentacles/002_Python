import requests
import telebot

from io import BytesIO

from telebot import TeleBot
from telebot.types import CallbackQuery
from urllib.parse import quote


from buttons import get_main_keyboard
from buttons import get_new_keyboard
from logger import logger
from models import UserRequest

from config import API_KEY
from config import BOT_TOKEN

from config import API_KEY
from config import BOT_TOKEN


bot = telebot.TeleBot(BOT_TOKEN)

# bot = telebot.TeleBot(BOT_TOKEN)
user_response = {}


def user_input_title(bot: telebot, call: CallbackQuery):
    """отправляет сообщение пользователю и регистрирует следующий шаг 
    обработчика ввода
    """  

    bot.send_message(call.message.chat.id, 'Введи название фильма')
    bot.register_next_step_handler(call.message, create_url, bot)
        




def create_url(call, bot):

    chat_id = call.chat.id

    # это нужно дальше изменить на вид - фильм: данные
    user_response[chat_id] = call.text.strip()
    
    logger.info(
        f'Пользователь ищет фильм по названию {call.text.strip()}.'
    )

    user_title = call.text.strip()
    encoding_title = quote(user_title)

    # Получить введенное пользователем название и закодировать:
    user_title = call.text.strip()
    encoding_title = quote(user_title)

    url = (
        f'https://api.kinopoisk.dev/v1.4/movie/search?page=1&limit=1&'
        f'query={encoding_title}'
    )


    get_search_content(bot, url, chat_id)
    keyboard = get_new_keyboard()
    bot.send_message(
        chat_id, 'МЕНЮ НОВИНКИ   '
        'Выбери тип новинок или вернись в главное меню:', 
        reply_markup=keyboard
    )



def get_search_content(bot, url, chat_id):

    bot.send_message(chat_id, 'сейчас найдем')

    



if __name__ == '__main__':
    bot.infinity_polling()
