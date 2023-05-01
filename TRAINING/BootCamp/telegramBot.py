# Для установки на macOS нам надо написать в терминале
# pip3 install pyTelegramBotAPI

import telebot
token = "5813295603:AAF3y5Y2XUZDz-dzXfyl8evXBrm3ZHMADQg"

# В этой строчке мы заводим бота и даем ему запомнить токен
bot = telebot.TeleBot(token)