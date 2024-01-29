"""Модуль получения истории запросов пользователя из models.py."""


from typing import List

from telebot import TeleBot
from telebot.types import CallbackQuery

from keyboards.inline import get_main_keyboard
from logger import logger
from models import UserRequest


def show_history(bot: TeleBot, call: CallbackQuery,
                 user_name: str, user_id: str) -> None:
    """Выводит краткую историю запросов пользователя.

    Args:
        bot (TeleBot): Экземпляр бота.
        call (CallbackQuery): Callback-запрос от пользователя.
        user_name (str): Имя пользователя.
    """
    history_entries = get_user_history(user_name, user_id)
    
    if history_entries:
        history_text = '\n'.join(history_entries)
        bot.send_message(
            call.message.chat.id,
            f'История запросов пользователя:\n{history_text}',
        )
    else:
        bot.send_message(
            call.message.chat.id,
            'История запросов пользователя пуста.',
        )

    bot.send_message(
        call.message.chat.id,
        'ГЛАВНОЕ МЕНЮ',
        reply_markup=get_main_keyboard()
    )


def get_user_history(user_name: str, user_id: str) -> List[str]:
    """Получаем историю запросов пользователя.

    Args:
        user_id (str): Идентификатор пользователя.

    Returns:
        List[str]: Список строк с историей запросов пользователя.
    """
    try:
        history_entries = (
            UserRequest
            .select()
            .where(UserRequest.user_name == user_name)
            .where(UserRequest.user_id == user_id)
            .order_by(UserRequest.timestamp.desc())
            .limit(10)
        )
        history_text = [
            f'{entry.timestamp.strftime("%Y-%m-%d %H:%M:%S")}\t| '
            f'user: {entry.user_name}\t| '
            f'id: {entry.user_id}\t| '
            f'{entry.category}'
            for entry in history_entries
        ]

        logger.info(
            f'История запросов пользователя {user_name}: {history_text}'
        )

        return history_text
    except Exception as exc:
        logger.error(
            f'Ошибка получения истории пользователя: {exc}', exc_info=True
        )
        return []
