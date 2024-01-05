"""
Модуль для загрузки переменных окружения из файла .env.

Этот модуль содержит код для проверки наличия файла .env
и загрузки переменных окружения из него с использованием
библиотек os и dotenv.

Примечание:
    Для корректной работы требуется установка библиотеки dotenv.
    Установка: pip install python-dotenv
"""


import os
import sys

from dotenv import find_dotenv
from dotenv import load_dotenv

# Проверяем, есть ли файл .env, и загружаем переменные окружения из него:
if find_dotenv is None:
    sys.exit('Переменные окружения не загружены, так как отсутствует файл .env')
else:
    load_dotenv()

# Получаем значения переменных окружения:
USERNAME = os.getenv('USERNAME')
BOT_TOKEN = os.getenv('BOT_TOKEN')
API_KEY = os.getenv('API_KEY')
