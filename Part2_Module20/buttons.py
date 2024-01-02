import telebot
from telebot import types
from config import BOT_TOKEN
from new import get_new_movies


bot = telebot.TeleBot(BOT_TOKEN)
user_states = {}


@bot.message_handler(commands=["new"])
def ask_user(message):

    user_id = message.from_user.id
    user_states[user_id] = {'command': 'new'}

    # кнопки выбора:
    print("выбираю кнопку")
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.KeyboardButton("Фильмы"))
    keyboard.add(types.KeyboardButton("Сериалы"))
    keyboard.add(types.KeyboardButton("Мультфильмы"))

    # запрос у пользователя нажать кнопку:
    bot.send_message(user_id, "Выбири тип", reply_markup=keyboard)
    # bot.register_next_step_handler(message, user_choice)
    print("запуск функции с парам", message.text)


    # скрываем клавиатуру после выбора пользователя
    # hide_markup = types.ReplyKeyboardRemove()
    # bot.send_message(chat_id, reply_markup=hide_markup)




# @bot.message_handler(func=lambda message: True)
# def all_message(message):
#     if message.text.lower() in ["фильмы", "сериалы", "мультфильмы"]:
#         user_choice(message)
#     else:
#         bot.send_message(message.chat.id, "Неизвестная команда. Пожалуйста, используйте кнопки.")

# @bot.message_handler(content_types=["KeyboardButton"])
# def user_movie(message):
#         print(message.text)
#         url = "https://api.kinopoisk.dev/v1.4/movie?page=1&limit=5&type=movie&year=2023"
#         print("https://api.kinopoisk.dev/v1.4/movie?page=1&limit=5&type=movie&year=2023")
#         return url



@bot.message_handler(func=lambda message: message.text.lower() in ["фильмы", "сериалы", "мультфильмы"])
def user_choice(message):
    print("запуск функции с парам", message.text)
    user_id = message.from_user.id
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