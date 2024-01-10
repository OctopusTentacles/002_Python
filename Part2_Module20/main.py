"""Этот модуль содержит основной код для бота Telegram."""


import telebot

from buttons import get_main_keyboard
from buttons import get_new_keyboard
from config import BOT_TOKEN
from new import get_new_url
from high import get_top_url
from models import UserRequest
from logger import logger
from history import show_history

bot = telebot.TeleBot(BOT_TOKEN)
usernames_dict = {}

@bot.message_handler(commands=['start'])
def welcome(message: telebot.types.Message) -> None:
    """Приветственное сообщение бота. Реагирует при запуске и по команде /start.

    Args:
        message (telebot.types.Message): Сообщение от пользователя.
    """
    try:
        user_id = message.from_user.id
        username = message.from_user.first_name
        # Сохранение имени пользователя для использования в истории:
        usernames_dict[user_id] = username

        # Сохранение запроса пользователя в базу данных:
        UserRequest.create(
            user_name=str(username),
            user_id=str(user_id), 
            category='start'
        )
        keyboard = get_main_keyboard()
        bot.send_message(message.chat.id,
                        f'Привет, {username}!\n'
                        f'Выбери одну из команд:',
                        reply_markup=keyboard
        )
        logger.info(f'Команда /start для '
                    f'пользователя {username} с ID {user_id}.'
        )
    except Exception as exc:
        logger.error(f'Ошибка в обработчике команды '
                     f'/start: {exc}', exc_info=True
        )

@bot.callback_query_handler(func=lambda call: True)
def main_menu(call: telebot.types.CallbackQuery) -> None:
    """Основное меню бота.

    Args:
        call (telebot.types.CallbackQuery): Callback-запрос от пользователя.
    """
    try:
        user_id = call.from_user.id
        username = usernames_dict.get(user_id)

        if call.data == 'новинки':
            category = 'новинки'
            ask_user_buttons(call)

            if call.data in ['фильм', 'сериал', 'мульт', 'main']:  # noqa: WPS510
                category = call.data
                get_new_url(call.message.chat.id, category)


        if call.data == 'топ':
            category = 'топ'
            ask_user_buttons(call)

            if call.data in ['фильм', 'сериал', 'мульт', 'main']:  # noqa: WPS510
                category = call.data
                get_top_url(call.message.chat.id, category)


        if call.data == 'history':
            category = 'history'
            show_history(bot, call, username, user_id)




        # Сохранение запроса пользователя в базу данных:
        UserRequest.create(
            user_name=str(username),
            user_id=str(user_id),
            category=category
        )

        logger.info(f'Обработан callback-запрос от '
                    f'пользователя {username} с ID {user_id}.'
        )
    except Exception as exc:
        logger.error(f'Ошибка в обработчике '
                     f'callback-запроса: {exc}', exc_info=True
        )


def ask_user_buttons(call: telebot.types.CallbackQuery) -> None:
    """Запрос от бота для выбора типа контента.

    Args:
        call (telebot.types.CallbackQuery): Callback-запрос от пользователя.
    """
    try:
        keyboard = get_new_keyboard()
        bot.send_message(call.message.chat.id, 'Выбери тип', 
                         reply_markup=keyboard)

        logger.info(f'Отправлен запрос от бота для выбора типа контента '
                    f'пользователю {call.from_user.id}.'
        )
    except Exception as exc:
        logger.error(f'Ошибка в функции ask_user_buttons: '
                     f'{exc}', exc_info=True
        )


if __name__ == '__main__':
    bot.infinity_polling()
