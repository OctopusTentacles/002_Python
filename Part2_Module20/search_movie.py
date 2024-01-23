import requests
import telebot

from io import BytesIO

from telebot import TeleBot
from telebot.types import CallbackQuery
from urllib.parse import quote


from buttons import get_main_keyboard
from logger import logger
from models import UserRequest

from config import API_KEY
from config import BOT_TOKEN


bot = telebot.TeleBot(BOT_TOKEN)

user_response = {}


def user_input_title(bot: telebot, call: CallbackQuery):
    """отправляет сообщение пользователю и регистрирует следующий шаг 
    обработчика ввода.
    
    Args:
        bot (TeleBot): Экземпляр бота.
        call (CallbackQuery): Callback-запрос от пользователя.
    """  

    bot.send_message(call.message.chat.id, 'Введи название фильма')
    bot.register_next_step_handler(call.message, create_url, bot)


def create_url(call, bot):
    """Обработчик ввода, формирует URL для поиска фильма."""

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
    get_search_content(bot, url, chat_id)
    keyboard = get_main_keyboard()
    bot.send_message(chat_id, "ГЛАВНОЕ МЕНЮ", reply_markup=keyboard)


def get_search_content(bot, url, chat_id):
    """Выполняет поиск фильма и отправляет результат пользователю."""
    bot.send_message(chat_id, 'сейчас найдем')

    headers = {"accept": "application/json", "X-API-KEY": API_KEY}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        contents = data.get('docs')

        for content in contents:
            poster = content.get('poster', {}).get('previewUrl')
            title = content.get('name')
            year = content.get('year')
            length = content.get('movieLength')

            genres_data = content.get('genres', [])
            genres = ', '.join(genre.get('name') for genre in genres_data)
            
            countries_data = content.get('countries',  [])
            countries = ', '.join(country.get('name') for country in countries_data)

            description = content.get('description')

            rate_kp = content.get('rating', {}).get('kp')
            rate_imdb = content.get('rating', {}).get('imdb')


            image_io = BytesIO(requests.get(poster).content)
            message_text = (
                f'{title}   ({year})\n\n'
                f'жанр: {genres}.\n\n'
                f'страна: {countries}.\n\n'
                f'{description}.\n\n'
                f'длительность: {length} мин.\n\n'
                f'КП: {rate_kp}\n'
                f'IMDB: {rate_imdb}'
            )

            bot.send_photo(chat_id, image_io, caption=message_text)
            logger.info(
                f'Пользователь получил данные по: {title}.'
            )


    else:
        logger.error(
            f'Ошибка при получении данных. Код ответа: {response.status_code}'
        )
        bot.send_message(chat_id, 'Прости, неполадки, давай еще раз...')


if __name__ == '__main__':
    bot.infinity_polling()
