# 1. Создание бота, который реагирует на команду /hello-world, а также на текст
# «Привет» (необходимо сообщить проверяющему куратору имя вашего бота для
# тестирования).


import telebot
from config import USERNAME, BOT_TOKEN, API_KEY


bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(content_types=["text"])
def start_message(message):
    bot.send_message(message.chat.id, message.text)



# MAIN==================================================
if __name__ == "__main__":
    bot.infinity_polling()