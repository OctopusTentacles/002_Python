"""Модуль для настройки логирования в боте.

param:
    sink - если установлен по умолчанию, то логи будут направляться
    в стандартный поток вывода (stdout), что означает вывод в консоль.
    sink = None - логгер отправляет логи в стандартный поток
    ошибок (stderr), что может быть полезным, например,
    при запуске бота в фоновом режиме.
"""


import os
# import sys

from loguru import logger

# Получение текущего каталога, где находится скрипт:
cur_dir = os.path.dirname(__file__)

# Настройка логирования в файл bot.log:
logger.add(
    os.path.join(cur_dir, 'bot.log'),
    rotation='10 MB',
    level='INFO',
    sink=None
)
