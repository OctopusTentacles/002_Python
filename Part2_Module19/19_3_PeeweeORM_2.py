# Peewee + pyTelegramBotAPI

# Рассмотрим интеграцию Peewee и pyTelegramBotAPI на примере менеджера задач.

# Менеджер задач будет иметь три команды:
# /newtask — создать задачу,
# /tasks — показать последние десять задач,
# /today — показать задачи на сегодня.

# Конфигурационный файл
# Определим константы, которые понадобятся нам в дальнейшей работе:
# путь к базе данных
DB_PATH = "database.db"
# этот токен нужно получить при создании бота у @BotFather
BOT_TOKEN = "<ТОКЕН_ТЕЛЕГРАМ_БОТА>"
# поддерживаемые команды
DEFAULT_COMMANDS = (
    ("newtask", "Создать задачу"),
    ("tasks", "Последние 10 задач"),
    ("today", "Задачи на сегодня"),
)
# формат назначенной даты у задачи
DATE_FORMAT = "%d.%m.%Y"

# Модели
# Опишем модели, которые нам понадобятся. Сначала создадим базовый класс BaseModel:
class BaseModel(Model):
    class Meta:
        database = db

# Создадим модель пользователя:
class User(BaseModel):
    user_id = IntegerField(primary_key=True)
    username = CharField()
    first_name = CharField()
    last_name = CharField(null=True)
# user_id — первичный ключ модели, будет совпадать с Telegram ID. Это значит, 
    # что он будет уникальным для всей таблицы.
# username — никнейм в Telegram.
# first_name — имя в Telegram.
# last_name — фамилия в Telegram. Может быть не указана, поэтому ставим null=True.

# Создадим модель задачи:

class Task(BaseModel):
    task_id = AutoField()
    user = ForeignKeyField(User, backref="tasks")
    title = CharField()
    due_date = DateField()
    is_done = BooleanField(default=False)

    def __str__(self):
        return "{task_id}. {check} {title} - {due_date}".format(
            task_id=self.task_id,
            check="[V]" if self.is_done else "[ ]",
            title=self.title,
            due_date=self.due_date.strftime(DATE_FORMAT),
        )
    
# task_id — ID задачи. AutoField показывает, что это первичный ключ, 
    # а значение будет автоматически увеличиваться на единицу. 
    # Аналог PRIMARY KEY AUTOINCREMENT.
# user — внешний ключ, ссылающийся на пользователя; backref создаёт обратную 
    # ссылку: мы сможем получить задачи пользователя с помощью user.tasks.
# title — название задачи.
# due_date — назначенная дата выполнения задачи.
# is_done — указание, выполнена ли задача.
# В методе __str__ мы переопределили вывод задачи в текстовом виде, 
    # чтобы это можно было удобно использовать в дальнейшем.

# Введём вспомогательную функцию, которая создаст все наши модели в базе данных:
def create_models():
    db.create_tables(BaseModel.__subclasses__())
# BaseModel.__subclassess__() вернёт список наследников класса BaseModel.
    
# 