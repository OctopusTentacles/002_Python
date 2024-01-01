

import telebot
from telebot import types
import requests
from config import USERNAME, BOT_TOKEN, API_KEY


bot = telebot.TeleBot(BOT_TOKEN)
cached_movie = set()


def get_new_movies(chat_id, url):

    # url = "https://api.kinopoisk.dev/v1.4/movie"
    # url = "https://api.kinopoisk.dev/v1.4/movie?page=1&limit=100&notNullFields=&type=movie&premiere.world=01.01.2023-28.12.2023"
    # url = "https://api.kinopoisk.dev/v1.4/movie?page=1&limit=5&type=cartoon&year=2023"

    # url = buttons.ask_user(message)
    # if url is not None:
    headers = {"accept": "application/json", "X-API-KEY": API_KEY}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        movies = data.get("docs")

        count = 0
        message_text = "Список 5 новых фильмов в этом году:\n"

        for movie in movies:
            title = movie.get("name")
                
            if title not in cached_movie and count < 5:
                cached_movie.add(title)
                count += 1
                message_text += f"Фильм: {title}\n"

        bot.send_message(chat_id, message_text)
    else:
        print(f"Ошибка при получении данных. Код ответа: {response.status_code}")



if __name__ == "__main__":
    bot.infinity_polling()