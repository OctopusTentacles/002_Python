""""""

import os
from peewee import Model, SqliteDatabase, CharField, DateTimeField
from datetime import datetime


# Получение текущего каталога, где находится скрипт:
cur_dir = os.path.dirname(__file__)

# Инициализация базы данных (SQLite) в каталоге скрипта:
db = SqliteDatabase(os.path.join(cur_dir, 'user_history.db'))


class UserRequest(Model):
    """
    Модель для запросов пользователя.

    Attributes:
        user_name (CharField): Имя пользователя.
        user_id (CharField): Идентификатор пользователя.
        category (CharField): Категория запроса.
        timestamp (DateTimeField): Временная метка запроса - текущее время.
    """
    user_name = CharField()
    user_id = CharField()
    category = CharField()
    timestamp = DateTimeField(default=datetime.now)

    class Meta:
        database = db


# Инициализация таблицы в базе данных
db.connect()
db.create_tables([UserRequest])
db.close()
