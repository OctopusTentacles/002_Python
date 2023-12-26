import os
from dotenv import load_dotenv, find_dotenv

# Проверяем, есть ли файл .env, и загружаем переменные окружения из него:
if not find_dotenv:
    exit("Переменные окружения не загружены, так как отсутствует файл .env")
else:
    load_dotenv()

# Получаем значения переменных окружения:
USERNAME = os.getenv("USERNAME")
BOT_TOKEN = os.getenv("BOT_TOKEN")
API_KEY = os.getenv("API_KEY")

# print(USERNAME, BOT_TOKEN, API_KEY)