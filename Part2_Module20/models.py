""""""

from peewee import Model, SqliteDatabase, CharField, DateTimeField
from datetime import datetime


# Инициализация базы данных (SQLite)
db = SqliteDatabase('user_history.db')


class UserRequest(Model):
    """
    Модель для запросов пользователя.

    Attributes:
        user_id (CharField): Идентификатор пользователя.
        category (CharField): Категория запроса.
        timestamp (DateTimeField): Временная метка запроса - текущее время.
    """
    user_id = CharField()
    category = CharField()
    timestamp = DateTimeField(default=datetime.now)

    class Meta:
        database = db


# Инициализация таблицы в базе данных
db.connect()
db.create_tables([UserRequest])