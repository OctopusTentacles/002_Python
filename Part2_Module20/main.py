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
from rand import get_random_url
from search_movie import user_input_title

bot = telebot.TeleBot(BOT_TOKEN)
usernames_dict = {}
user_states = {}

def set_user_state(user_id, category):
    user_states[user_id] = {"category": category}

def get_user_state(user_id):
    return user_states.get(user_id, {"category": "start"})


@bot.message_handler(commands=['start'])
def welcome(message: telebot.types.Message) -> None:
    """Приветственное сообщение бота. Реагирует при запуске и по команде /start.

    Args:
        message (telebot.types.Message): Сообщение от пользователя.
    """
    try:
        user_id = message.from_user.id
        username = message.from_user.first_name

        # Используем машину состояний, чтобы получить текущую категорию пользователя
        current_state = get_user_state(user_id)
        category_old = current_state["category"]

        # Сохраняем имя пользователя и устанавливаем начальное состояние (категорию)
        usernames_dict[user_id] = username
        set_user_state(user_id, "start")

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

        # Используем машину состояний, чтобы получить текущую категорию пользователя
        current_state = get_user_state(user_id)
        category_old = current_state["category"]

        # Устанавливаем значение по умолчанию для переменной category
        category = None



        if call.data == 'новинки':
            set_user_state(user_id, 'новинки')
            ask_user_buttons(call)
            category = 'новинки'

        elif call.data == 'топ':
            set_user_state(user_id, 'топ')
            ask_user_buttons(call)
            category = 'топ'

        elif call.data == 'history':
            set_user_state(user_id, 'history')
            show_history(bot, call, username, user_id)
            category = 'history'

        elif call.data == 'random':
            set_user_state(user_id, 'random')
            ask_user_buttons(call)
            category = 'random'

        elif call.data == 'search_movie':
            set_user_state(user_id, 'search_movie')
            user_input_title(call.message.chat.id, category)



        elif call.data in ['фильм', 'сериал', 'мульт', 'main']:
            category = call.data

            if category_old == 'новинки':
                get_new_url(call.message.chat.id, category)
            elif category_old == 'топ':
                get_top_url(call.message.chat.id, category)
            elif category_old == 'random':
                get_random_url(call.message.chat.id, category)

        # Сохранение запроса пользователя в базу данных:
        UserRequest.create(
            user_name=str(username),
            user_id=str(user_id),
            category=category
        )

        logger.info(f'Переход из {category_old} в {category}\t|'
                    f' {username} | ID {user_id}.'
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
