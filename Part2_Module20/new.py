import telebot
import requests
from config import BOT_TOKEN, API_KEY

bot = telebot.TeleBot(BOT_TOKEN)
cached_movie = set()

def get_new_movies(chat_id, url):
    print("запуск get movies")
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