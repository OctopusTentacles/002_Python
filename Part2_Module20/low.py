
import telebot
import requests
from config import USERNAME, BOT_TOKEN, API_KEY


bot = telebot.TeleBot(BOT_TOKEN)
cached_movie = set()


def ask_user(message):
    

@bot.message_handler(commands=["low"])
def get_low_movies(message):

    url = "https://api.kinopoisk.dev/v1.4/movie"
    headers = {"accept": "application/json", "X-API-KEY": API_KEY}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()


        ask_user(message)