# поменял команду LOW на NEW - самые новые фильмы.


import telebot
import requests
from config import API_KEY


bot = telebot.TeleBot(API_KEY)


bot.message_handler(commands=["new"])
def new_films(message):

    url = "https://api.kinopoisk.dev/v1.4/movie?page=1&limit=3&year=2023-2024"
    headers = {"accept": "application/json", "X-API-KEY": API_KEY}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        movies = data.get("docs")

        message_text = "Список 10 самых новых фильмов:\n"

        for movie in movies:
            title = movie.get("name")
            message_text += f"Фильм: {title}\n"

        bot.send_message(message.chat.id, message_text)
