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
        bot.send_message(chat_id, 'введи название фильма')
        query = 
        
        url = (
            f'https://api.kinopoisk.dev/v1.4/movie/search?page=1&limit=1&'
            f'query=%D1%82%D0%B5%D1%80%D0%BC%D0%B8%D0%BD%D0%B0%D1%82%D0%BE%D1%80'
        )

    