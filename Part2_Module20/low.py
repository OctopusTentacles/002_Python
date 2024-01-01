
import telebot
import requests
from telebot import types
from config import USERNAME, BOT_TOKEN, API_KEY


bot = telebot.TeleBot(BOT_TOKEN)
cached_movie = set()

@bot.message_handler(commands=["new"])
def ask_user(message):

    chat_id = message.chat.id
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.KeyboardButton("Фильмы"))
    keyboard.add(types.KeyboardButton("Сериалы"))
    keyboard.add(types.KeyboardButton("Мультфильмы"))

    


