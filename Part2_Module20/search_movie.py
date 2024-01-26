"""Модуль поиска контента по названию."""

import requests
import telebot
import base64

from io import BytesIO

from telebot.types import CallbackQuery
from urllib.parse import quote


from buttons import get_main_keyboard
from logger import logger
from models import UserRequest

from config import API_KEY

cached_content = {}


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
    search_content(bot, url, chat_id)
    keyboard = get_main_keyboard()
    bot.send_message(chat_id, "ГЛАВНОЕ МЕНЮ", reply_markup=keyboard)


def search_content(bot, url, chat_id):
    """Получает ссылку с краткой информацией о контенте из слов пользователя.
    Берем из нее ID и формируем ссылку о контенте с полной информацией.
        
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
            if id not in cached_content:
                url = f'https://api.kinopoisk.dev/v1.4/movie/{id}'

                get_content_from_url(bot, url, chat_id, id)
            
            else:
                cached_data = cached_content.get(id, {})
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
                        chat_id, f'ПРОСТИ, ПОСТЕРА НЕТ!\n\n{cachaed_text_1}'
                    )
                    bot.send_message(chat_id, cachaed_text_2[:4096])
                    if len(cachaed_text_2) > 4096:
                        bot.send_message(chat_id, cachaed_text_2[4096:])

                    logger.info(
                        f'Пользователь получил данные из кэша БЕЗ ПОСТЕРА.'
                    )



def get_content_from_url(bot, url, chat_id, id):
    """Получает ссылку с полной информацией о контенте.
    Берет нужные элементы и формирует сообщение для пользователя.
    Также ложит данные в кэш.
        
    Args:
        bot (TeleBot): Экземпляр бота.
        url: полная ссылка на контент.
        chat_id: .
        id: номер контента.
    """

    headers = {"accept": "application/json", "X-API-KEY": API_KEY}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        contents = [data]

        for content in contents:


            poster = content.get('poster', {}).get('previewUrl')
            title = content.get('name')
            year = content.get('year')

            premiere_data = content.get('premiere', {}).get('world')
            if premiere_data:
                premiere = premiere_data.split('T')[0]
            else:
                premiere = 'неизвестно'
               

            movieLength = content.get('movieLength')
            seriesLength = content.get('seriesLength')
            if movieLength is None and seriesLength is None:
                length = 0
            elif seriesLength is None:
                length = movieLength
            else:
                length = seriesLength


            persons_data = content.get('persons', [])
            directors = ', '.join(
                person['name'] for person in persons_data 
                if person['profession'] == 'режиссеры' and
                person['name'] is not None
            )
            actors = ', '.join(
                person['name'] for person in persons_data
                if person['profession'] == 'актеры' and
                person['name'] is not None
            )

            genres_data = content.get('genres', [])
            genres = ', '.join(genre.get('name') for genre in genres_data)
            
            countries_data = content.get('countries',  [])
            countries = ', '.join(country.get('name') for country in countries_data)

            description = content.get('description')

            rate_kp = content.get('rating', {}).get('kp')
            rate_imdb = content.get('rating', {}).get('imdb')

            trailers_data = content.get('videos', {}).get('trailers', [])
            if trailers_data:
                trailer = trailers_data[0].get('url', '')
            else:
                trailer = 'не сняли'


            message_text_1 = (
                f'{title}   ({year})\n\n'
                f'премьера: {premiere}\n\n'
                f'жанр: {genres}.\n\n'
                f'страна: {countries}.\n\n'
            )
            message_text_2 = (
                f'режиссер: {directors}\n'
                f'актеры: {actors}\n\n'
                f'{description}.\n\n'
                f'длительность: {length} мин.\n\n'
                f'КП: {rate_kp}\n'
                f'IMDB: {rate_imdb}\n\n'
                f'трейлер: {trailer}'
            )

            if poster:
                image_io = BytesIO(requests.get(poster).content)
                # положить в кэш по id - message_text и poster:
                poster_b64 = base64.b64encode(image_io.getvalue()).decode('utf-8')
                cached_content[id] = {
                    'poster': poster_b64,
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
                cached_content[id] = {
                    'poster': None,
                    'text_1': message_text_1,
                    'text_2': message_text_2
                }
                bot.send_message(chat_id, f'ПРОСТИ, ПОСТЕРА НЕТ!\n\n{message_text_1}')
                bot.send_message(chat_id, message_text_2[:4096])
                if len(message_text_2) > 4096:
                    bot.send_message(chat_id, message_text_2[4096:])
                logger.info(
                    f'Пользователь получил данные БЕЗ ПОСТЕРА по: {title}.'
                )

    else:
        bot.send_message(chat_id, 'Прости, неполадки, давай еще раз...')
        logger.error(
            f'Ошибка при получении данных. Код ответа: {response.status_code}'
        )


# if __name__ == '__main__':
#     bot.infinity_polling()
