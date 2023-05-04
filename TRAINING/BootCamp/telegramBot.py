# Для установки на macOS нам надо написать в терминале
# pip3 install pyTelegramBotAPI

import telebot
from pydub import AudioSegment


token = "5813295603:AAF3y5Y2XUZDz-dzXfyl8evXBrm3ZHMADQg"


# В этой строчке мы заводим бота и даем ему запомнить токен
bot = telebot.TeleBot(token)

# Пишем первую функцию, которая отвечает "Привет" на команду /start
# Все функции общения приложения с ТГ спрятаны в функции под @
@bot.message_handler(commands=['start'])

def say_hi(message):
    bot.send_message(message.chat.id, 'Привет ✌️ ' + message.chat.first_name)   #add user name

# Запускаем бота. Он будет работать до тех пор, пока работает ячейка (крутится значок слева).
# Остановим ячейку - остановится бот
bot.infinity_polling()

# Преобразование формата аудио oga → wav
# Телеграм отправляет голосовые в формате .oga, а SpeechRecognition нужен формат .wav.
# Напишем функцию для преобразования файла:
def oga2wav(filename):
    # Переименование формата: 'sample.oga' -> 'sample.wav'
    new_filename = ...
    # Читаем файл с диска с помощью функции AudioSegment.from_file()
    audio = ...
    # Экспортируем файл в новом формате
    audio.export(..., format=...)
    # Возвратим в качестве результата функции имя нового файла
    return ...