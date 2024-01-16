"""Модуль случайного выбора контента."""


import requests
import telebot

from io import BytesIO
from typing import List

from buttons import get_main_keyboard
from buttons import get_new_keyboard
from logger import logger

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

    if category == 'фильм':
        url = (
            f'https://api.kinopoisk.dev/v1.4/movie/random?'
            f'notNullFields=name&notNullFields=year&notNullFields=rating.kp&'
            f'notNullFields=poster.url&type=movie'
        )
        bot.send_message(chat_id, 'Случайный фильм:')

    elif category == 'сериал':
        url = (
            f'https://api.kinopoisk.dev/v1.4/movie/random?'
            f'notNullFields=name&notNullFields=year&notNullFields=rating.kp&'
            f'notNullFields=poster.url&notNullFields=backdrop.url&'
            f'notNullFields=logo.url&notNullFields=description&type=tv-series'
        )
        bot.send_message(chat_id, 'Случайный сериал:')

    elif category == 'мульт':
        url = (f'https://api.kinopoisk.dev/v1.4/movie/'
               f'random?notNullFields=name&type=cartoon'
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


def get_rand_content(chat_id, url):
    headers = {"accept": "application/json", "X-API-KEY": API_KEY}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        contents = [data]

        message_text = '\n'

        for content in contents:
            poster = content.get('poster', {}).get('previewUrl')
            backdrop = content.get('backdrop', {}).get('previewUrl')
            logo = content.get('logo', {}).get('url')

            print(poster, backdrop, logo)

            tittle = content.get('name')
            year = content.get('year')

            about = content.get('description')


            rate = content.get('rating', {}).get('kp')



        if tittle not in cached_content:
            cached_content.add(tittle)

            message_text = (
                    f'{tittle} ({year})\n\n'
                    f'{about}\n\n'
                    f'КП: {rate}'
                )

            poster_io = BytesIO(requests.get(poster).content)
            backdrop_io = BytesIO(requests.get(backdrop).content)
            logo_io = BytesIO(requests.get(logo).content)
            media = [
                telebot.types.InputMediaPhoto(media=poster_io),
                telebot.types.InputMediaPhoto(media=backdrop_io),
                telebot.types.InputMediaPhoto(media=logo_io)
            ]


            bot.send_media_group(chat_id, media)
            bot.send_message(chat_id, message_text)

    else:
        logger.error(
            f'Ошибка при получении данных. Код ответа: {response.status_code}'
        )
        bot.send_message(chat_id, 'Прости, у меня неполадки!')


if __name__ == "__main__":
    bot.infinity_polling()
