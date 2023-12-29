# поменял команду LOW на NEW - самые новые фильмы.


import telebot
import requests
from config import API_KEY


bot = telebot.TeleBot(API_KEY)


bot.message_handler(commands=["new"])
def new_films(message):

    url = "https://api.kinopoisk.dev/v1.4/movie?page=1&limit=10&year=2023-2024"
    headers = {"accept": "application/json", "X-API-KEY": API_KEY}

    response = requests.get(url, headers=headers)


    