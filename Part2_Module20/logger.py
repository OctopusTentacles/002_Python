"""Модуль для настройки логирования в боте.

param:
    rotation - размер файла bot.log.
    level - уровень логирования от INFO и выше.
"""


import os

from loguru import logger

# Получение текущего каталога, где находится скрипт:
cur_dir = os.path.dirname(__file__)

# Удаление стандартного логгера чтобы избавиться от вывода в консоль:
logger.remove()

# Настройка логирования в файл bot.log:
logger.add(
    os.path.join(cur_dir, 'bot.log'),
    rotation='10 MB',
    level='INFO',
)
