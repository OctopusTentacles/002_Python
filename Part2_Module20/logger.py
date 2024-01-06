"""Модуль для настройки логирования в боте."""


import os

from loguru import logger

# Получение текущего каталога, где находится скрипт:
cur_dir = os.path.dirname(__file__)


# Настройка логирования в файл bot.log:
logger.add(os.path.join(cur_dir, 'bot.log'), rotation='10 MB', level='INFO')
