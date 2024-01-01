
import telebot
import requests
from telebot import types
from config import USERNAME, BOT_TOKEN, API_KEY
from new import get_new_movies

bot = telebot.TeleBot(BOT_TOKEN)
cached_movie = set()

@bot.message_handler(commands=["new"])
def ask_user(message):

    chat_id = message.chat.id

    # кнопки выбора:
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.KeyboardButton("Фильмы"))
    keyboard.add(types.KeyboardButton("Сериалы"))
    keyboard.add(types.KeyboardButton("Мультфильмы"))

    # запрос у пользователя:
    msg = bot.send_message(chat_id, "Выбири тип", reply_markup=keyboard)
    bot.register_next_step_handler(msg, user_choise, get_new_movies)


def user_choise(message, next_function):
    chat_id = message.chat.id
    user_choice = message.text.lower()

    url = None
    if user_choice == "фильмы":
        url = "https://api.kinopoisk.dev/v1.4/movie?page=1&limit=5&type=movie&year=2023"

    elif user_choice == "сериалы":
        url = "https://api.kinopoisk.dev/v1.4/movie?page=1&limit=5&type=tv-series&year=2023"

    elif user_choice == "мультфильмы":
        url = "https://api.kinopoisk.dev/v1.4/movie?page=1&limit=5&type=cartoon&year=2023"

    if url is not None:
        next_function(chat_id, url)



