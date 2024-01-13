"""Модуль случайного выбора контента."""


import requests
import telebot

from typing import List

from buttons import get_main_keyboard
from buttons import get_new_keyboard

from config import API_KEY
from config import BOT_TOKEN

bot = telebot.TeleBot(BOT_TOKEN)
cached_content = set()


def get_random_url(chat_id, category: str):
    """Получает случайный фильм/сериал/мультфильм с некоторой информацией.

    Args:
        category (str): Категория запроса ('movie', 'tv', 'animation').

    Returns:
        List[str]: Список строк с названиями и рейтингами.
    """
    url = None
    # url = "https://api.kinopoisk.dev/v1.4/movie/random"
    # url = "https://api.kinopoisk.dev/v1.4/movie?page=1&limit=3&type=movie&rating.kp=6-10"

    if category == 'фильм':
        url = (
             
        )
        bot.send_message(chat_id, 'Случайный фильм:')

    elif category == 'сериал':
        url = (
             
        )
        bot.send_message(chat_id, 'Случайный сериал:')

    elif category == 'мульт':
        url = (
             
        )
        bot.send_message(chat_id, 'Случайный мультфильм:')

    elif category == 'main':
        keyboard = get_main_keyboard()
        bot.send_message(chat_id, 'ГЛАВНОЕ МЕНЮ', reply_markup=keyboard)

    if url is not None:
        get_rand_content(chat_id, url)
        keyboard = get_new_keyboard()
        bot.send_message(
            chat_id, 
            'Выбери тип или вернись в главное меню:',
            reply_markup=keyboard
        )



    
                
                


if __name__ == "__main__":
    bot.infinity_polling()