# 1. Создание бота, который реагирует на команду /hello-world, а также на текст
# «Привет» (необходимо сообщить проверяющему куратору имя вашего бота для
# тестирования).


import telebot
from config import USERNAME, BOT_TOKEN, API_KEY


bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands = ["start", "help"])
def welcome(message):
    bot.reply_to(message, "Hello world")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)


# MAIN==================================================
if __name__ == "__main__":
    bot.infinity_polling()