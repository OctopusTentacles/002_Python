# Для установки на macOS нам надо написать в терминале
# pip3 install pyTelegramBotAPI

import speech_recognition
import telebot
from pydub import AudioSegment
import os


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

import urllib

url = "https://drive.google.com/uc?export=view&id=1aBZnHgsjg7XIVlvpYasOOJ8hurp7V6Ww"
filename = "skillbox_voice_sample.ogg"
urllib.request.urlretrieve(url, filename)

recognizer = ...

with speech_recognition.WavFile('skillbox_voice_sample.wav') as source:     
     wav_audio = ...

recognizer.recognize_google(..., language='ru')

# Вылетит ошибка, если файл не найден
os.remove('skillbox_voice_sample.wav')

# Правим ошибку: добавляем условие
# Если файл существует - удалить с диска
def recognize_speech(oga_filename):
    wav_filename = oga2wav(oga_filename)
    recognizer = speech_recognition.Recognizer()

    with speech_recognition.WavFile(wav_filename) as source:     
        wav_audio = recognizer.record(source)

    text = recognizer.recognize_google(wav_audio, language='ru')

    if os.path.exists(oga_filename):
        os.remove(oga_filename)

    if os.path.exists(wav_filename):
        os.remove(wav_filename)

    return text
recognize_speech('skillbox_voice_sample.oga')