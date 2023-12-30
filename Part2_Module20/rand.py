
import telebot
import requests
from config import USERNAME, BOT_TOKEN, API_KEY


bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=["random"])
def get_random_film(message):
    url = "https://api.kinopoisk.dev/v1.4/movie/random"
    headers = {"accept": "application/json", "X-API-KEY": API_KEY}
    
    while True:
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()

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
                
                if title and kp_rate > 7:
                    bot.send_message(message.chat.id,   f"Фильм с рейтингом больше 7:\n"
                                                        f"{title}\n" 
                                                        f"Рейтинг КП: {kp_rate}\n"
                                                        f"год: {year}\n")
                    break
            else:
                bot.send_message(message.chat_id, f'''Ошибка при получении данных. 
                                Код ответа: {response.status_code}''')
                break

        except requests.exceptions.RequestException as exc:
            bot.send_message(message.chat.id, f'''Произошла ошибка при получении 
                            случайного фильма: {exc}''')

if __name__ == "__main__":
    bot.infinity_polling()