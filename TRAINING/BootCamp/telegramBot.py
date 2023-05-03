# Для установки на macOS нам надо написать в терминале
# pip3 install pyTelegramBotAPI

import telebot

token = "5813295603:AAF3y5Y2XUZDz-dzXfyl8evXBrm3ZHMADQg"

# В этой строчке мы заводим бота и даем ему запомнить токен
bot = telebot.TeleBot(token)

# Пишем первую функцию, которая отвечает "Привет" на команду /start
# Все функции общения приложения с ТГ спрятаны в функции под @
@bot.message_handler(commands=['start'])

def say_hi(message):
    bot.send_message(message.chat.id, 'Привет ✌️ ')

# Запускаем бота. Он будет работать до тех пор, пока работает ячейка (крутится значок слева).
# Остановим ячейку - остановится бот
bot.infinity_poling()