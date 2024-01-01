import telebot
from telebot import types
from config import BOT_TOKEN
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

    # передаем ссылку на функцию get_new_movies в параметре дополнительных данных
    bot.register_next_step_handler(msg, user_choise)

def user_choise(message):
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
        get_new_movies(chat_id, url)

if __name__ == "__main__":
    bot.infinity_polling()