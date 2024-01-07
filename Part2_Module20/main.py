"""Этот модуль содержит основной код для бота Telegram."""


import telebot

from buttons import get_main_keyboard
from buttons import get_new_keyboard
from config import BOT_TOKEN
from new import get_new_url
from models import UserRequest
from logger import logger
from history import show_history

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message: telebot.types.Message) -> None:
    """Приветственное сообщение бота. Реагирует при запуске и по команде /start.

    Args:
        message (telebot.types.Message): Сообщение от пользователя.
    """
    username = message.from_user.first_name
    keyboard = get_main_keyboard()
    bot.send_message(message.chat.id,
                     f'Привет, {username}!\nВыбери одну из команд:',
                     reply_markup=keyboard
                     )
    # Сохранение запроса пользователя в базу данных
    UserRequest.create(user_id=str(message.from_user.id), category='start')

@bot.callback_query_handler(func=lambda call: True)
def main_menu(call: telebot.types.CallbackQuery) -> None:
    """Основное меню бота.

    Args:
        call (telebot.types.CallbackQuery): Callback-запрос от пользователя.
    """
    category = None

    if call.data == 'новинки':
        category = 'новинки'
        # Сохранение запроса пользователя в базу данных
        UserRequest.create(user_id=str(call.message.from_user.id), category=category)
        ask_user_buttons(call)

    elif call.data == 'history':
        category = 'history'
        # Сохранение запроса пользователя в базу данных
        UserRequest.create(user_id=str(call.message.from_user.id), category=category)
        show_history(bot,call)

    elif call.data in ['фильм', 'сериал', 'мульт', 'main']:  # noqa: WPS510
        category = call.data

    if category is not None:
        get_new_url(call.message.chat.id, category)

    # Сохранение запроса пользователя в базу данных
    UserRequest.create(user_id=str(call.message.from_user.id), category=category)



def ask_user_buttons(call: telebot.types.CallbackQuery) -> None:
    """Запрос от бота для выбора типа контента.

    Args:
        call (telebot.types.CallbackQuery): Callback-запрос от пользователя.
    """
    keyboard = get_new_keyboard()
    bot.send_message(call.message.chat.id, 'Выбери тип', reply_markup=keyboard)


if __name__ == '__main__':
    bot.infinity_polling()
