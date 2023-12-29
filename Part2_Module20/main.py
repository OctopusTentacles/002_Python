# 1. Создание бота, который реагирует на команду /hello-world, а также на текст
# «Привет» (необходимо сообщить проверяющему куратору имя вашего бота для
# тестирования).

import telebot
import requests
from config import USERNAME, BOT_TOKEN, API_KEY


bot = telebot.TeleBot(BOT_TOKEN)


bot.message_handler(commands=["random"])
def random_film(message):
    api_url = "https://api.kinopoisk.dev/v1.4/movie/random"
    headers = {"accept": "application/json",
              "X-API-KEY": API_KEY
              }

    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        # Извлечь нужные данные из объекта `data`:
        title = data.get("name")
        # rating = data.get("rating")



        bot.send_message(message.chat.id, response.text)
    else:
         print("Ошибка соединения")
          






@bot.message_handler(commands=["get_data"])
def get_data(message):
    api_url = "https://api.kinopoisk.dev"
    params = {"api_key": API_KEY, "chat_id": message.chat.id}
    # try:
        # Отправка GET-запроса к API:
    response = requests.get(api_url)
    if response.status_code == 200:
            data = response.json()
            bot.send_message(message.chat.id, f"Получены данные: {data}")

@bot.message_handler(commands=["hello-world"])
def greet_message(message):
    username = message.from_user.first_name
    bot.send_message(message.chat.id, f"Hello-{username}!")

@bot.message_handler(content_types=["text"])
def hello(message):
    username = message.from_user.first_name
    if message.text.lower().startswith("привет"):
        bot.send_message(message.chat.id, f"Привет, {username}!")


# MAIN==================================================
if __name__ == "__main__":
    bot.infinity_polling()