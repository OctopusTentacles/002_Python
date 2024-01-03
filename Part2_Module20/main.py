import telebot
from telebot import types
from config import BOT_TOKEN
# from generate_api import ask_user_buttons


bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=["start"])
def welcome(message):
    username = message.from_user.first_name

    keyboard = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(text="Новинки", callback_data="новинки")
    button2 = types.InlineKeyboardButton(text="Случайный фильм", callback_data="рандом")
    keyboard.add(button1, button2)

    bot.send_message(message.chat.id, 
                        f"Привет, {username}!\n"
                        f"Выбери одну из команд:",
                        reply_markup=keyboard,
                    )

@bot.callback_query_handler(func=lambda call: True)
def main_new(call):

    if call.data == "новинки":
        ask_user_buttons(call)
    elif call.data == "фильм":
        url = "https://api.kinopoisk.dev/v1.4/movie?page=1&limit=5&type=movie&year=2023"
        bot.send_message(call.message.chat.id, url)
        
    elif call.data == "сериал":
        url = "https://api.kinopoisk.dev/v1.4/movie?page=1&limit=5&type=tv-series&year=2023"
        bot.send_message(call.message.chat.id, url)

    elif call.data == "мульт":
        url = "https://api.kinopoisk.dev/v1.4/movie?page=1&limit=5&type=cartoon&year=2023"
        bot.send_message(call.message.chat.id, url)



def ask_user_buttons(call):
    print("перешли в новинки")

    keyboard = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(text="Фильмы", callback_data="фильм")
    button2 = types.InlineKeyboardButton(text="Сериалы", callback_data="сериал")
    button3 = types.InlineKeyboardButton(text="Мультфильмы", callback_data="мульт")
    keyboard.add(button1, button2, button3)

    bot.send_message(call.message.chat.id, "Выбери тип", reply_markup=keyboard)


if __name__ == "__main__":
    bot.infinity_polling()
