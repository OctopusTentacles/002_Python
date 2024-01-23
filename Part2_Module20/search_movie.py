import requests
import telebot

from io import BytesIO

from telebot import TeleBot
from telebot.types import CallbackQuery
from urllib.parse import quote


from buttons import get_main_keyboard
from buttons import get_new_keyboard
from logger import logger
from models import UserRequest

<<<<<<< HEAD
from config import API_KEY
from config import BOT_TOKEN
=======
from urllib.parse import quote
>>>>>>> 90b65c851aa37de34fb5a8f835b5360fbc52edd2

from config import API_KEY
from config import BOT_TOKEN


bot = telebot.TeleBot(BOT_TOKEN)

# bot = telebot.TeleBot(BOT_TOKEN)
user_response = {}


<<<<<<< HEAD
def user_input_title(bot: telebot, call: CallbackQuery):
    """отправляет сообщение пользователю и регистрирует следующий шаг 
    обработчика ввода
=======

def user_input_title(call: CallbackQuery,
                 user_name: str, user_id: str):
    """Отправляет сообщение пользователю и 
    регистрирует следующий шаг обработчика ввода.

    Args:
        bot (TeleBot): Экземпляр бота.
        call (CallbackQuery): Callback-запрос от пользователя.
        user_name (str): Имя пользователя.
>>>>>>> 90b65c851aa37de34fb5a8f835b5360fbc52edd2
    """  

    bot.send_message(call.message.chat.id, 'Введи название фильма')
    bot.register_next_step_handler(call.message, create_url, bot)
        



<<<<<<< HEAD

def create_url(call, bot):
=======
def create_url(call):
>>>>>>> 90b65c851aa37de34fb5a8f835b5360fbc52edd2

    chat_id = call.chat.id

    # это нужно дальше изменить на вид - фильм: данные
    user_response[chat_id] = call.text.strip()
    
    logger.info(
        f'Пользователь ищет фильм по названию {call.text.strip()}.'
    )

    user_title = call.text.strip()
    encoding_title = quote(user_title)

    # Получить введенное пользователем название и закодировать:
    user_title = call.text.strip()
    encoding_title = quote(user_title)

    url = (
        f'https://api.kinopoisk.dev/v1.4/movie/search?page=1&limit=1&'
        f'query={encoding_title}'
    )


    get_search_content(chat_id, url)
    keyboard = get_new_keyboard()
    bot.send_message(
        call.message.chat.id, 'МЕНЮ НОВИНКИ   '
        'Выбери тип новинок или вернись в главное меню:', 
        reply_markup=keyboard
    )

    get_search_movie(bot, call, url)


def get_search_movie(bot, call, url):
    print('in def get_search_movie')

    bot.send_message(call.message.chat.id, 'сейчас найдем')



<<<<<<< HEAD
# if __name__ == '__main__':
#     bot.infinity_polling()
=======


def get_search_content(chat_id, url):
    headers = {'accept': 'application/json', 'X-API-KEY': API_KEY}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        contents = data.get('docs')

        print('docs')

    pass

if __name__ == '__main__':
    bot.infinity_polling()
>>>>>>> 90b65c851aa37de34fb5a8f835b5360fbc52edd2
