
import telebot
import requests
from telebot import types
from config import USERNAME, BOT_TOKEN, API_KEY


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
    bot.send_message(chat_id, "Выбири тип", reply_markup=keyboard)
    bot.register_next_step_handler(message, user_choise)


def user_choise(message):
    chat_id = message.chat.id
    user_choice = message.text.lower()

    if user_choice == "фильмы":
        url = "https://api.kinopoisk.dev/v1.4/movie?page=1&limit=5&type=movie&year=2023"

    if user_choice == "сериалы":
        url = "https://api.kinopoisk.dev/v1.4/movie?page=1&limit=5&type=tv-series&year=2023"

    if user_choice == "мультфильмы":
        url = "https://api.kinopoisk.dev/v1.4/movie?page=1&limit=5&type=cartoon&year=2023"

    return url



