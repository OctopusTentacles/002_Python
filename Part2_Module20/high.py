"""Модуль топ фильмов/сериалов/мультфильмов"""


import requests
import telebot

from typing import List

from buttons import get_main_keyboard
from buttons import get_new_keyboard

from config import API_KEY
from config import BOT_TOKEN

bot = telebot.TeleBot(BOT_TOKEN)
cached_content = set()


def get_top_url(chat_id, category: str) -> List[str]:
    """Получает топ фильмов/сериалов/мультфильмов с самым высоким рейтингом.

    Args:
        category (str): Категория запроса ('movie', 'tv', 'animation').

    Returns:
        List[str]: Список строк с названиями и рейтингами.
    """
    url = None

    if category == 'фильм':
        url = "https://api.kinopoisk.dev/v1.4/movie?page=1&limit=100&type=movie&rating.kp=9-10"
        bot.send_message(chat_id, 'Топ фильмов')

    elif category == 'сериал':
        url = "https://api.kinopoisk.dev/v1.4/movie?page=1&limit=100&type=tv-series&rating.kp=9-10"
        bot.send_message(chat_id, 'Топ сериалов')

    elif category == 'мульт':
        url = "https://api.kinopoisk.dev/v1.4/movie?page=1&limit=100&type=cartoon&rating.kp=9-10"
        bot.send_message(chat_id, 'Топ мультфильмов')

    elif category == 'main':
        keyboard = get_main_keyboard()
        bot.send_message(chat_id, 'ГЛАВНОЕ МЕНЮ', reply_markup=keyboard)

    if url is not None:
        get_top_rated(chat_id, url)
        keyboard = get_new_keyboard()
        bot.send_message(
            chat_id, 
            'Выбери тип или вернись в главное меню:',
            reply_markup=keyboard
        )


def get_top_rated(chat_id, url):
    headers = {"accept": "application/json", "X-API-KEY": API_KEY}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        contents = data.get('docs')

        count = 0
        message_text = '\n'

        for content in contents:
            title = content.get('name')
            rate = content.get('rating')
            rate_kp = rate.get('kp')

            if title not in cached_content and count < 10:
                cached_content.add(title)
                count += 1
                message_text += f'{count}: {title} рейтинг КП - {rate_kp}\n'

        bot.send_message(chat_id, message_text)
    else:
        print(f"Ошибка при получении данных. Код ответа: {response.status_code}")


if __name__ == '__main__':
    bot.infinity_polling()