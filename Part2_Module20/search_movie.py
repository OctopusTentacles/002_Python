import requests
import telebot

from io import BytesIO

from telebot import TeleBot
from telebot.types import CallbackQuery


from buttons import get_main_keyboard
from buttons import get_new_keyboard
from logger import logger
from models import UserRequest

from urllib.parse import quote

# from config import API_KEY
# from config import BOT_TOKEN


user_response = {}



def user_input_title(bot: TeleBot, call: CallbackQuery,
                 user_name: str, user_id: str):
    """Отправляет сообщение пользователю и 
    регистрирует следующий шаг обработчика ввода.

    Args:
        bot (TeleBot): Экземпляр бота.
        call (CallbackQuery): Callback-запрос от пользователя.
        user_name (str): Имя пользователя.
    """  

    bot.send_message(call.message.chat.id, 'Введи название фильма')
    bot.register_next_step_handler(call.message, create_url)
        


def create_url(call):

    chat_id = call.chat.id

    # это нужно дальше изменить на вид - фильм: данные
    user_response[chat_id] = call.text.strip()
    
    logger.info(
        f'Пользователь ищет фильм по названию {call.text.strip()}.'
    )
    print(user_response[chat_id])

    # Получить введенное пользователем название и закодировать:
    user_title = call.text.strip()
    encoding_title = quote(user_title)

    url = (
        f'https://api.kinopoisk.dev/v1.4/movie/search?page=1&limit=1&'
        f'query={encoding_title}'
    )


def get_search_content():


if __name__ == '__main__':
    bot.infinity_polling()
