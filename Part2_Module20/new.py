# поменял команду LOW на NEW - самые новые фильмы.


import telebot
import requests
from config import USERNAME, BOT_TOKEN, API_KEY


bot = telebot.TeleBot(BOT_TOKEN)


bot.message_handler(commands=["new"])
def get_new_movies(message):

    url = "https://api.kinopoisk.dev/v1.4/movie?page=1&limit=10&year=2023-2024"
    # url = "https://api.kinopoisk.dev/v1.4/movie?page=1&limit=10&year=&premiere.world=01.06.2023-28.12.2023"
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

if __name__ == "__main__":
    bot.infinity_polling()