"""Модуль для работы с базой данных и определения модели запросов пользователя."""


import os
from datetime import datetime

from peewee import CharField
from peewee import DateTimeField
from peewee import Model
from peewee import SqliteDatabase

# Получение текущего каталога, где находится скрипт:
cur_dir = os.path.dirname(__file__)

# Инициализация базы данных (SQLite) в каталоге скрипта:
db = SqliteDatabase(os.path.join(cur_dir, 'user_history.db'))


class UserRequest(Model):
    """Модель для запросов пользователя.

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

    class Meta(type):
        """Метакласс для указания базы данных.

        Attributes:
            database = db указывает, что объект базы данных db,
            созданный с использованием SqliteDatabase, будет
            использоваться для хранения данных модели UserRequest.
        """

        database = db


# Инициализация таблицы в базе данных
db.connect()
db.create_tables([UserRequest])
db.close()
