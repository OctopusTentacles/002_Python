"""Модуль поиска фильма/сеериала/мультфильма"""


import requests
import telebot

from io import BytesIO

from buttons import get_main_keyboard
from buttons import get_new_keyboard
from logger import logger

from config import API_KEY
from config import BOT_TOKEN


bot = telebot.TeleBot(BOT_TOKEN)


def get_search_movie_url(chat_id, category: str):
    """
    """
    if category == 'main':
        keyboard = get_main_keyboard()
        bot.send_message(chat_id, 'ГЛАВНОЕ МЕНЮ', reply_markup=keyboard)

    else:
        @bot.message_handler(content_types=['text'])
        # def get_text(message):
        message = bot.send_message(chat_id, 'Введи название фильма')
        bot.register_next_step_handler(message)


        # Получаем введенное пользователем название фильма
        query = message.text.strip()

        url = (
            f'https://api.kinopoisk.dev/v1.4/movie/search?page=1&limit=1&'
            f'query={query}'
        )

    