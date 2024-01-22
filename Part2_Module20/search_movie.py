import requests
import telebot

from io import BytesIO

from telebot import TeleBot
from telebot.types import CallbackQuery


from buttons import get_main_keyboard
from buttons import get_new_keyboard
from logger import logger
from models import UserRequest

# from config import API_KEY
# from config import BOT_TOKEN


user_response = {}


def get_search_movie(bot: TeleBot, call: CallbackQuery,
                 user_name: str, user_id: str):
        

        bot.send_message(
             call.message.chat.id,
             f'Введи название фильма'
        )

        print(1)

        bot.register_next_step_handler(call.message, user_input_title)
        
        logger.info(f'Отправлен запрос от бота для выбора типа контента '
                    f'пользователю {call.message}.'
        )
        print(2)

def user_input_title(message):
    """Функция срабатывает автоматически при отправке текстового сообщения"""

    print(3)

    chat_id = message.chat.id

    user_response[chat_id] = message.text.strip()
    print(user_response[chat_id])

    print(4)

    create_url(message)

def create_url(chat_id):
    # Получаем введенное пользователем название фильма
    query = user_response.get(chat_id, '')

    print(5)

    url = (
        f'https://api.kinopoisk.dev/v1.4/movie/search?page=1&limit=1&'
        f'query={query}'
    )

    print('ссылка поиска', query)


# if __name__ == '__main__':
#     bot.infinity_polling()
