# 1. Создание бота, который реагирует на команду /hello-world, а также на текст
# «Привет» (необходимо сообщить проверяющему куратору имя вашего бота для
# тестирования).


import telebot
import requests
from config import USERNAME, BOT_TOKEN, API_KEY
from buttons import ask_user
from rand import get_random_film


bot = telebot.TeleBot(BOT_TOKEN)

# приветствие:
welcome_message = set()
@bot.message_handler(commands=["start"])
def welcome(message):
    chat_id = message.chat.id
    username = message.from_user.first_name

    if chat_id not in welcome_message:
        bot.send_message(chat_id, f"Привет, {username}!\n"
                                f"пока только эти команды\n"
                                f"/new\n"
                                f"/random")
        welcome_message.add(chat_id)


@bot.message_handler(commands=["new"])
def main_new_movies(message):
    ask_user(message)


@bot.message_handler(commands=["random"])
def main_random_film(message):
    get_random_film(message)



# MAIN==================================================
if __name__ == "__main__":
    bot.infinity_polling()