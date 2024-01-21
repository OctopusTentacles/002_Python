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
def user_input_title(chat_id):
    """функция срабатывает автоматически при отправке текстового сообщения"""

    user_response[chat_id] = chat_id.strip()
    print(user_response[chat_id])
    
    # # Сохранение запроса пользователя в базу данных:
    # UserRequest.create(
    #     user_name=str(message.from_user.first_name),
    #     user_id=str(message.from_user.id),
    #     category='search_movie'
    # )

    create_url(chat_id)

def create_url(chat_id):
    # Получаем введенное пользователем название фильма
    query = user_response.get(chat_id, '')

    url = (
        f'https://api.kinopoisk.dev/v1.4/movie/search?page=1&limit=1&'
        f'query={query}'
    )

    print('ссылка поиска', query)





if __name__ == '__main__':
    bot.infinity_polling()
