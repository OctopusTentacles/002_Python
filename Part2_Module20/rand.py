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

    if category == 'фильм':
        url = (f'https://api.kinopoisk.dev/v1.4/movie/'
               f'random?notNullFields=name&notNullFields=year&'
               f'notNullFields=rating.kp&type=movie'
        )
        bot.send_message(chat_id, 'Случайный фильм:')

    elif category == 'сериал':
        url = (f'https://api.kinopoisk.dev/v1.4/movie/'
               f'random?notNullFields=name&type=tv-series'
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

    if response == 200:
        data = response.json()
        contents = data.get('docs')

        message_text = '\n'

        for content in contents:
            tittle = content.get('name')
            poster = content.get('poster', {}).get('url')


        # "poster": {
        #     "url": "https://avatars.mds.yandex.net/get-kinopoisk-image/4716873/ccc5d1a9-a7fd-44e4-b1f6-a5b031c886a5/orig",
        #     "previewUrl": "https://avatars.mds.yandex.net/get-kinopoisk-image/4716873/ccc5d1a9-a7fd-44e4-b1f6-a5b031c886a5/x1000"
        # }



            rate = content.get('rating')
            rate_kp = rate.get('kp')

            year = content.get('year')


            if tittle not in cached_content:
                cached_content.add(tittle)

                message_text = (
                    f'{tittle}\nгод: {year}\nрейтинг КП: {rate_kp}'
                )
        bot.send_photo(chat_id, photo=InputFile(poster))
        bot.send_message(chat_id, message_text)
    else:
        print(f"Ошибка при получении данных. Код ответа: {response.status_code}")


if __name__ == "__main__":
    bot.infinity_polling()
