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
def user_input_title(message):
    """
    """    
    message = bot.send_message(message.chat.id, 'Введи название фильма')
    bot.register_next_step_handler(message, create_url)
    print('user message', message.text)


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
        user_input_title()


    





if __name__ == '__main__':
    bot.infinity_polling()