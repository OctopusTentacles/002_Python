# 19.2 Библиотека pyTelegramBotAPI

# Онбординг
# Хорошие примеры
# П: «Привет!»
# Б: «Привет! Я виртуальный ассистент компании XXX. Я отвечу на ваши вопросы о компании, 
# нашей продукции, помогу сделать заказ. Какой у вас вопрос?»
# П: «Привет!»
# Б: «Привет! Я бот по поиску отелей. Смогу подобрать для вас подходящие отели, где бы 
# вы ни были. В каком городе хотите найти отель? Для подробного описания моих 
# возможностей напишите /help».

# Подсказки
# Хороший пример
# Б: «Результаты по вашему запросу:...
# Для продолжения введите новый запрос или одну из следующих команд:...».

# Обработка ошибок
# Хорошие примеры
# Б: «Выберите количество товаров».
# П: «Сколько времени?»
# Б: «Извините, я вас не понимаю. Введите количество товаров или 
# напишите /help для получения справки».
# Б: «Выберите количество товаров».
# П: «750».
# Б: «Ожидается число от 1 до 100».

# Вариативность
# Хороший пример
# П: «Привет, бот!»
# Б: «Рад вас снова видеть, Александр!»

# =======================================================================================
# Разработка телеграм-бота

# Простейший бот выглядит так:
import telebot
bot = telebot.TeleBot("TOKEN")
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Hello world!")
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)
if __name__ == '__main__':
    bot.infinity_polling()

# На команды /start и /help он ответит любимым приветствием. 
# А на всё остальное повторит то, что написал пользователь.
func=lambda message: True

# Для отправки сообщения используется команда send_message:
bot.send_message(message.chat.id, 'Новое сообщение!')

# =======================================================================================
# Хранение секретных данных
# Токен лучше не хранить прямо в коде, потому что злоумышленники могут им 
# воспользоваться, взяв его из вашего репозитория. Есть два основных способа 
# хранить секретные данные.

# Использовать отдельный модуль config.py с объявленными переменными 
# BOT_TOKEN, API_KEY и подобными.
# Дополнительно использовать переменные окружения. 
# На практике это реализуется с помощью .env-файла и библиотеки python-dotenv:
# .env:
BOT_TOKEN = "ajdu3qjbkjasd3"
API_KEY = "asdjnahd1he2dsa"

# config.py:
import os
from dotenv import load_dotenv, find_dotenv
if not find_dotenv():
    exit("Переменные окружения не загружены, так как отсутствует файл .env")
else:
    load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
API_KEY = os.getenv("API_KEY")

# =======================================================================================
# Навигация

# Возникает вопрос: что, если, помимо команд, пользователь должен вводить какие-то 
# данные, с которыми впоследствии нужно что-то сделать? 
# Здесь также есть два основных способа навигации.

#  1 register_next_step_handler
#  После обработки сообщения мы явно указываем следующий обработчик:
@bot.message_handler(commands=['start'])
def welcome(message):
    mesg = bot.send_message(message.chat.id, 'Введите имя')
    bot.register_next_step_handler(mesg, test)

def test(message):
    name = message.text
    bot.send_message(message.chat.id, f'Ваше имя: {name}')

# 2 Состояния
    #https://github.com/eternnoir/pyTelegramBotAPI/blob/master/examples/custom_states.py

# Этот способ работает по принципу автомата состояний: мы знаем, в каком состоянии 
# сейчас находимся, но не знаем, как мы тут оказались.

# В документации библиотеки приведён отличный пример. 
# В классе MyStates мы указываем состояния, в которых можем оказаться (строка 31). 
# С помощью декораторов обозначаем, какое состояние должно обрабатываться 
# (строки 50, 58, 69, 80, 94) и куда необходимо перейти с помощью set_state 
# (строка 45). Дополнительно нужно добавить StateFilter в качестве фильтра
# (строка 103) и инициализировать хранилище состояний (строка 24).
    
# =======================================================================================
# Хранение данных
# В том же примере реализовано хранение данных на основе контекстного менеджера 
# retrieve_data, с помощью которого можно взаимодействовать с данными текущего 
# пользователя (строки 65, 76, 85). Плюс в том, что нам не нужно использовать 
# глобальные переменные и за нас заранее разграничили данные между пользователями, 
# так что здесь можно безопасно хранить любую информацию.

# =======================================================================================
# Работа с кнопками
# Чтобы пользователю было удобно проходить ваш сценарий, не вводя вручную какую-либо 
# информацию, можно использовать кнопки.

# InlineKeyboardMarkup — callback-кнопки, при нажатии на которые пользователь 
# получает нужную информацию. В callback можно записать текст.