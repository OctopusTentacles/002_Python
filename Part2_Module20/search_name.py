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


def user_input_title(bot: telebot, call: CallbackQuery) -> None:
    """отправляет сообщение пользователю и регистрирует следующий шаг 
    обработчика ввода.
    
    Args:
        bot (TeleBot): Экземпляр бота.
        call (CallbackQuery): Callback-запрос от пользователя.
    """  

    bot.send_message(call.message.chat.id, 'Введи имя:')
    bot.register_next_step_handler(call.message, create_url, bot)
