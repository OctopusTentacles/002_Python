from typing import List
from models import UserRequest
from telebot.types import CallbackQuery
from telebot import TeleBot


def show_history(bot: TeleBot, call: CallbackQuery, 
                 user_name: str, user_id: str) -> None:
    """Выводит краткую историю запросов пользователя.

    Args:
        bot (TeleBot): Экземпляр бота.
        call (CallbackQuery): Callback-запрос от пользователя.
        username (str): Имя пользователя.
    """
    history_entries = get_user_history(user_name, user_id)
    
    if history_entries:
        history_text = '\n'.join(history_entries)
        bot.send_message(call.message.chat.id,
                         f'История запросов пользователя:\n{history_text}'
                         )
    else:
        bot.send_message(call.message.chat.id,
                         f'История запросов пользователя пуста.'
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
            f'{entry.timestamp.strftime("%Y-%m-%d %H:%M:%S")} | '
            f'user: {entry.user_name} | '
            f'id: {entry.user_id} | '
            f'{entry.category}'
            for entry in history_entries
        ]


        return history_text
    except Exception as exc:
        print(f'Ошибка получения истории пользователя: {exc}')
        return []
