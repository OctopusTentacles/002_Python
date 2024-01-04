import telebot
from config import BOT_TOKEN
from buttons import get_main_keyboard, get_new_keyboard
from new import get_new_movies


bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=["start"])
def welcome(message):
    username = message.from_user.first_name
    keyboard = get_main_keyboard()
    bot.send_message(message.chat.id, f"Привет, {username}!\n"
                     f"Выбери одну из команд:", reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def main_menu(call):
    url = None

    if call.data == "новинки":
        ask_user_buttons(call)
    
    elif call.data == "фильм":
        url = "https://api.kinopoisk.dev/v1.4/movie?page=1&limit=100&type=movie&year=2023"
        bot.send_message(call.message.chat.id, "5 новых фильмов:")

    elif call.data == "сериал":
        url = "https://api.kinopoisk.dev/v1.4/movie?page=1&limit=100&type=tv-series&year=2023"
        bot.send_message(call.message.chat.id, "5 новых сериалов:")

    elif call.data == "мульт":
        url = "https://api.kinopoisk.dev/v1.4/movie?page=1&limit=100&type=cartoon&year=2023"
        bot.send_message(call.message.chat.id, "5 новых мультфильмов:")

    if url is not None:
        get_new_movies(call.message.chat.id, url)
        ask_user_buttons(call)


def ask_user_buttons(call):
    keyboard = get_new_keyboard()
    bot.send_message(call.message.chat.id, "Выбери тип", reply_markup=keyboard)


if __name__ == "__main__":
    bot.infinity_polling()
