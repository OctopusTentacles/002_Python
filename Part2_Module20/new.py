import requests
import telebot

from io import BytesIO

from buttons import get_main_keyboard
from buttons import get_new_keyboard
from config import API_KEY
from config import BOT_TOKEN

bot = telebot.TeleBot(BOT_TOKEN)
cached_movie = set()


def get_new_url(chat_id, category):

    url = None

    if category == "фильм":
        url = (
            f'https://api.kinopoisk.dev/v1.4/movie?page=1&limit=100&'
            f'selectFields=name&selectFields=year&selectFields=poster&'
            f'notNullFields=name&notNullFields=poster.url&'
            f'sortField=year&sortType=-1&type=movie&year=2023-2024'
        )
        bot.send_message(chat_id, "5 новых фильмов:")

    elif category == "сериал":
        url = (
            f'https://api.kinopoisk.dev/v1.4/movie?page=1&limit=100&'
            f'selectFields=name&selectFields=year&selectFields=poster&'
            f'notNullFields=name&notNullFields=poster.url&'
            f'sortField=year&sortType=-1&type=tv-series&year=2023-2024'
        )
        bot.send_message(chat_id, "5 новых сериалов:")

    elif category == "мульт":
        url = (
            f'https://api.kinopoisk.dev/v1.4/movie?page=1&limit=100&'
            f'selectFields=name&selectFields=year&selectFields=poster&'
            f'notNullFields=name&notNullFields=poster.url&'
            f'sortField=year&sortType=-1&type=cartoon&year=2023-2024'
        )
        bot.send_message(chat_id, "5 новых мультфильмов:")

    elif category == "main":
        keyboard = get_main_keyboard()
        bot.send_message(chat_id, "ГЛАВНОЕ МЕНЮ", reply_markup=keyboard)

    if url is not None:
        get_new_movies(chat_id, url)
        keyboard = get_new_keyboard()
        bot.send_message(
            chat_id, 'НОВИНКИ   '
            'Выбери тип новинок или вернись в главное меню:', 
            reply_markup=keyboard
        )


def get_new_movies(chat_id, url):
    headers = {"accept": "application/json", "X-API-KEY": API_KEY}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        contents = data.get('docs')

        count = 0

        for content in contents:
            poster = content.get('poster', {}).get('previewUrl')
            title = content.get('name')
            year = content.get('year')
                
            if title not in cached_movie and count < 5:
                cached_movie.add(title)
                count += 1

                message_text = f"{count}: {title} ({year})\n"
                image_io = BytesIO(requests.get(poster).content)

                bot.send_photo(chat_id, image_io, caption=message_text)
    else:
        print(f"Ошибка при получении данных. Код ответа: {response.status_code}")


if __name__ == "__main__":
    bot.infinity_polling()
