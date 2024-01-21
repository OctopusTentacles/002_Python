"""Модуль поиска фильма/сеериала/мультфильма"""


import requests
import telebot

from io import BytesIO

from buttons import get_main_keyboard
from buttons import get_new_keyboard
from logger import logger
from models import UserRequest

from config import API_KEY
from config import BOT_TOKEN


bot = telebot.TeleBot(BOT_TOKEN)
user_response = {}


def get_search_movie(chat_id, category: str):

    if category == 'main':
        keyboard = get_main_keyboard()
        bot.send_message(chat_id, 'ГЛАВНОЕ МЕНЮ', reply_markup=keyboard)

    elif category == 'search_movie':
        bot.send_message(chat_id, 'Введи название фильма')



@bot.message_handler(content_types=['text'])
def user_input_title(message):
    """функция срабатывает автоматически при отправке текстового сообщения"""

    user_response[message.chat.id] = message.text.strip()

    # Сохранение запроса пользователя в базу данных:
    UserRequest.create(
        user_name=str(username),
        user_id=str(user_id),
        category=category
    )


def create_url(message):
    # Получаем введенное пользователем название фильма
    query = message.text.strip()

    url = (
        f'https://api.kinopoisk.dev/v1.4/movie/search?page=1&limit=1&'
        f'query={query}'
    )

    print('ссылка поиска', query)





if __name__ == '__main__':
    bot.infinity_polling()
