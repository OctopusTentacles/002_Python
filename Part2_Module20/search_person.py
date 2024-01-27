"""Модуль поиска по имени."""

import base64
from io import BytesIO
from urllib.parse import quote

import requests
import telebot
from telebot.types import CallbackQuery

from buttons import get_main_keyboard
from config import API_KEY
from logger import logger
from models import UserRequest

cached_names = {}


def user_input_name(bot: telebot, call: CallbackQuery) -> None:
    """отправляет сообщение пользователю и регистрирует следующий шаг 
    обработчика ввода.
    
    Args:
        bot (TeleBot): Экземпляр бота.
        call (CallbackQuery): Callback-запрос от пользователя.
    """  

    bot.send_message(call.message.chat.id, 'Введи имя:')
    bot.register_next_step_handler(call.message, create_url, bot)


def create_url(call: CallbackQuery, bot: telebot) -> None:
    """Обработчик ввода, формирует URL для поиска человека по имени."""

    chat_id = call.chat.id
    logger.info(
        f'Пользователь ищет человека по имени: {call.text.strip()}.'
    )

    # Получить введенное пользователем название и закодировать:
    user_title = call.text.strip()
    encoding_title = quote(user_title)

    url = (
        f'https://api.kinopoisk.dev/v1.4/person/search?page=1&limit=1&'
        f'query={encoding_title}'
    )
    search_name(bot, url, chat_id)
    keyboard = get_main_keyboard()
    bot.send_message(chat_id, "ГЛАВНОЕ МЕНЮ", reply_markup=keyboard)


def search_name(bot: telebot, url: str, chat_id: int) -> str:
    """Получает ссылку с краткой информацией о человеке из слов пользователя.
    Берем из нее ID и формируем ссылку о человеке с полной информацией.
        
    Args:
        bot (TeleBot): Экземпляр бота.
        url: .
        chat_id: .
    """
    bot.send_message(chat_id, 'сейчас найдем')

    headers = {"accept": "application/json", "X-API-KEY": API_KEY}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        contents = data.get('docs')

        # получаем id для получения полной информации и кэширования:
        for content in contents:
            id = content.get('id')

            # если id нет в кэше 
            # создаем ссылку с полной инфо и отправляем на разбор:
            if id not in cached_names:
                url = f'https://api.kinopoisk.dev/v1.4/person/{id}'

                get_name_from_url(bot, url, chat_id, id)

            else:
                cached_data = cached_names.get(id, {})
                cached_poster = cached_data.get('poster', '')
                cachaed_text_1 = cached_data.get('text_1', '')
                cachaed_text_2 = cached_data.get('text_2', '')

                if cached_poster != None:
                    # декодирование постера:
                    poster_bytes = base64.b64decode(cached_poster)
                    poster_io = BytesIO(poster_bytes)
                    bot.send_photo(chat_id, poster_io, caption=cachaed_text_1)
                    bot.send_message(chat_id, cachaed_text_2[:4096])
                    if len(cachaed_text_2) > 4096:
                        bot.send_message(chat_id, cachaed_text_2[4096:])
                    
                    logger.info(
                        f'Пользователь получил данные из кэша.'
                    )
                else:
                    bot.send_message(
                        chat_id, f'ПРОСТИ, ФОТО НЕТ!\n\n{cachaed_text_1}'
                    )
                    bot.send_message(chat_id, cachaed_text_2[:4096])
                    if len(cachaed_text_2) > 4096:
                        bot.send_message(chat_id, cachaed_text_2[4096:])

                    logger.info(
                        f'Пользователь получил данные из кэша БЕЗ ФОТО.'
                    )
    else:
        bot.send_message(chat_id, 'Прости, неполадки, давай еще раз...')
        logger.error(
            f'Ошибка при получении данных. Код ответа: {response.status_code}'
        )


def get_name_from_url(bot: telebot, url: str, chat_id: int, id: int) -> None:
    """Получает ссылку с полной информацией о человеке.
    Берет нужные элементы и формирует сообщение для пользователя.
    Также ложит данные в кэш.
        
    Args:
        bot (TeleBot): Экземпляр бота.
        url: полная ссылка на контент.
        chat_id: .
        id: номер человека.
    """
    headers = {"accept": "application/json", "X-API-KEY": API_KEY}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        contents = [data]

        for content in contents:
            poster = content.get('photo')
            title = content.get('name')
            age = content.get('age')
            growth = content.get('growth')
            countAwards = content.get('countAwards')

            birthday_data = content.get('birthday')
            if birthday_data:
                birthday = birthday_data.split('T')[0]
            else:
                birthday = 'неизвестно'

            birthPlace_data = content.get('birthPlace', [])
            birthPlace = ', '.join(
                place['value'] for place in birthPlace_data
                if place['value'] is not None
            )

            profession_data = content.get('profession', [])
            profession = ', '.join(
                profi['value'] for profi in profession_data
                if profi['value'] is not None
            )

            facts_data = content.get('facts', [])
            facts = '\n'.join(
                fact['value'] for fact in facts_data
                if fact['value'] is not None
            )


# "death": null,
# "deathPlace": [],
            

            message_text_1 = (
                f'{title}   ({age})\n\n'
                f'дата рождения: {birthday}\n\n'
                f'место раждения: {birthPlace}\n\n'
                f'рост: {growth}\n\n'
                f'профессия: {profession}\n\n'
                f'количество наград: {countAwards}'
            )
            message_text_2 = (
                f'{facts}'
            )

            if poster:
                image_io = BytesIO(requests.get(poster).content)
                # положить в кэш по id - message_text и poster:
                poster_64 = base64.b64encode(image_io.getvalue()).decode('utf-8')
                cached_names[id] = {
                    'poster': poster_64,
                    'text_1': message_text_1,
                    'text_2': message_text_2
                }

                bot.send_photo(chat_id, image_io, caption=message_text_1)
                bot.send_message(chat_id, message_text_2[:4096])
                if len(message_text_2) > 4096:
                    bot.send_message(chat_id, message_text_2[4096:])
                logger.info(
                    f'Пользователь получил данные по: {title}.'
                )
            else:
                cached_names[id] = {
                    'poster': None,
                    'text_1': message_text_1,
                    'text_2': message_text_2
                }
                bot.send_message(chat_id, f'ПРОСТИ, ФОТО НЕТ!\n\n{message_text_1}')
                bot.send_message(chat_id, message_text_2[:4096])
                if len(message_text_2) > 4096:
                    bot.send_message(chat_id, message_text_2[4096:])
                logger.info(
                    f'Пользователь получил данные БЕЗ ФОТО по: {title}.'
                )


    else:
        bot.send_message(chat_id, 'Прости, неполадки, давай еще раз...')
        logger.error(
            f'Ошибка при получении данных. Код ответа: {response.status_code}'
        )