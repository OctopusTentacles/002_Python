"""Модуль поиска фильма/сеериала/мультфильма"""


import requests
import telebot

from io import BytesIO

from buttons import get_main_keyboard
from buttons import get_new_keyboard
from logger import logger

from config import API_KEY
from config import BOT_TOKEN


bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(content_types=['text'])
def user_input_title(chat_id):
    """
    """    
    # bot.send_message(chat_id, 'Введи название фильма')
    bot.register_next_step_handler_by_chat_id(chat_id, create_url)
    print('user message', chat_id)


def create_url(message):
    # Получаем введенное пользователем название фильма
    query = message.text.strip()

    url = (
        f'https://api.kinopoisk.dev/v1.4/movie/search?page=1&limit=1&'
        f'query={query}'
    )

    print('ссылка поиска', query)


def get_search_movie(chat_id, category: str):

    if category == 'main':
        keyboard = get_main_keyboard()
        bot.send_message(chat_id, 'ГЛАВНОЕ МЕНЮ', reply_markup=keyboard)

    elif category == 'search_movie':
        bot.send_message(chat_id, 'Введи название фильма')

        user_input_title(chat_id)



if __name__ == '__main__':
    bot.infinity_polling()
