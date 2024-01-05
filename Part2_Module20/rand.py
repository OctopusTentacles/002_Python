
import requests
import telebot

from config import API_KEY
from config import BOT_TOKEN
from config import USERNAME

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=["random"])
def get_random_film(message):

    url = "https://api.kinopoisk.dev/v1.4/movie/random"
    # url = "https://api.kinopoisk.dev/v1.4/movie?page=1&limit=3&type=movie&rating.kp=6-10"
    headers = {"accept": "application/json", "X-API-KEY": API_KEY}
    
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
                
                
        # Извлечь нужные данные из объекта `data`:
        title = data.get("name")
        rating = data.get("rating", {})
        kp_rate = rating.get("kp", "N/A")
        year = data.get("year")
        print(f"Фильм: {title}\n" 
                f"Рейтинг КП: {kp_rate}\n"
                f"год: {year}\n")
                
        bot.send_message(message.chat.id,   f"Фильм с рейтингом больше 7:\n"
                                                        f"{title}\n" 
                                                        f"Рейтинг КП: {kp_rate}\n"
                                                        f"год: {year}\n")


if __name__ == "__main__":
    bot.infinity_polling()