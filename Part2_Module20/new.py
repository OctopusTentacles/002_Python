

import telebot
import requests
from config import USERNAME, BOT_TOKEN, API_KEY

import buttons


bot = telebot.TeleBot(BOT_TOKEN)
cached_movie = set()





@bot.message_handler(commands=["new"])
def get_new_movies(message):

    # url = "https://api.kinopoisk.dev/v1.4/movie"
    # url = "https://api.kinopoisk.dev/v1.4/movie?page=1&limit=100&notNullFields=&type=movie&premiere.world=01.01.2023-28.12.2023"
    
    url = buttons.ask_user(message)
    headers = {"accept": "application/json", "X-API-KEY": API_KEY}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        movies = data.get("docs")

        count = 0
        message_text = "Список 10 новых фильмов в этом году:\n"

        for movie in movies:
            title = movie.get("name")
            
            if title not in cached_movie and count < 11:
                cached_movie.add(title)
                count += 1
                message_text += f"Фильм: {title}\n"

        bot.send_message(message.chat.id, message_text)

if __name__ == "__main__":
    bot.infinity_polling()