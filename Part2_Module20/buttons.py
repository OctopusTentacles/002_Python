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
    print("выбираю кнопку")
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.KeyboardButton("Фильмы"))
    keyboard.add(types.KeyboardButton("Сериалы"))
    keyboard.add(types.KeyboardButton("Мультфильмы"))

    # запрос у пользователя нажать кнопку:
    user_type = bot.send_message(chat_id, "Выбири тип", reply_markup=keyboard)
    bot.register_next_step_handler(user_type, user_choice)

    print("запуск функции с парам", message.text)

def user_choice(message):
    print("запуск функции с парам", message.text())
    chat_id = message.chat.id
    user_type = message.text.lower()
    print("функцию get_new_movies в параметре ")


    url = None
    if user_type == "Фильмы":
        url = "https://api.kinopoisk.dev/v1.4/movie?page=1&limit=5&type=movie&year=2023"
        print("https://api.kinopoisk.dev/v1.4/movie?page=1&limit=5&type=movie&year=2023"
)
    elif user_type == "Сериалы":
        url = "https://api.kinopoisk.dev/v1.4/movie?page=1&limit=5&type=tv-series&year=2023"

    elif user_type == "Мультфильмы":
        url = "https://api.kinopoisk.dev/v1.4/movie?page=1&limit=5&type=cartoon&year=2023"

    if url is not None:
        get_new_movies(chat_id, url)


if __name__ == "__main__":
    bot.infinity_polling()