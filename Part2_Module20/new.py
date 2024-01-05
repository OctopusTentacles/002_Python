import requests
import telebot

from buttons import get_main_keyboard
from buttons import get_new_keyboard
from config import API_KEY
from config import BOT_TOKEN

bot = telebot.TeleBot(BOT_TOKEN)
cached_movie = set()


def get_new_url(chat_id, category):

    url = None

    if category == "фильм":
        url = "https://api.kinopoisk.dev/v1.4/movie?page=1&limit=100&type=movie&year=2023"
        bot.send_message(chat_id, "5 новых фильмов:")

    elif category == "сериал":
        url = "https://api.kinopoisk.dev/v1.4/movie?page=1&limit=100&type=tv-series&year=2023"
        bot.send_message(chat_id, "5 новых сериалов:")

    elif category == "мульт":
        url = "https://api.kinopoisk.dev/v1.4/movie?page=1&limit=100&type=cartoon&year=2023"
        bot.send_message(chat_id, "5 новых мультфильмов:")

    elif category == "main":
        keyboard = get_main_keyboard()
        bot.send_message(chat_id, "ГЛАВНОЕ МЕНЮ", reply_markup=keyboard)

    if url is not None:
        get_new_movies(chat_id, url)
        keyboard = get_new_keyboard()
        bot.send_message(chat_id, "Выбери тип или назад:", reply_markup=keyboard)




def get_new_movies(chat_id, url):
    headers = {"accept": "application/json", "X-API-KEY": API_KEY}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        movies = data.get("docs")

        count = 0
        message_text = "\n"

        for movie in movies:
            title = movie.get("name")
                
            if title not in cached_movie and count < 5:
                cached_movie.add(title)
                count += 1
                message_text += f"{count}: {title}\n"

        bot.send_message(chat_id, message_text)
    else:
        print(f"Ошибка при получении данных. Код ответа: {response.status_code}")


if __name__ == "__main__":
    bot.infinity_polling()