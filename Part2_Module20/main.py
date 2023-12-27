# 1. Создание бота, который реагирует на команду /hello-world, а также на текст
# «Привет» (необходимо сообщить проверяющему куратору имя вашего бота для
# тестирования).


import telebot
from config import USERNAME, BOT_TOKEN, API_KEY


bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=["hello-world"])
def greet_message(message):
    username = message.from_user.first_name
    bot.send_message(message.chat.id, f"Привет, {username}!")



# MAIN==================================================
if __name__ == "__main__":
    bot.infinity_polling()