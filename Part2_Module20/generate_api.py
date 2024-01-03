# buttons.py
from telebot import types
from main import bot

user_states = {}

def ask_user_buttons(message):

    print("перешли в новинки")
    user_id = message.from_user.id
    user_states[user_id] = {'command': 'new'}

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton("Фильмы")
    button2 = types.KeyboardButton("Сериалы")
    button3 = types.KeyboardButton("Мультфильмы")

    keyboard.add(button1, button2, button3)

    bot.send_message(message.chat.id, "Выбери тип", reply_markup=keyboard)
    bot.register_next_step_handler(message, lambda msg: user_choice(msg, message))

def user_choice(message, original_message):
    user_id = message.from_user.id
    user_type = message.text.lower()

    url = None
    if user_type == "фильмы":
        url = "https://api.kinopoisk.dev/v1.4/movie?page=1&limit=5&type=movie&year=2023"
    elif user_type == "сериалы":
        url = "https://api.kinopoisk.dev/v1.4/movie?page=1&limit=5&type=tv-series&year=2023"
    elif user_type == "мультфильмы":
        url = "https://api.kinopoisk.dev/v1.4/movie?page=1&limit=5&type=cartoon&year=2023"

    if url is not None:
        get_new_movies(original_message.chat.id, url)


if __name__ == "__main__":
    bot.infinity_polling()
