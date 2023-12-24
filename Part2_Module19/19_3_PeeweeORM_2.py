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
    
# =======================================================================================
# Главный файл
# Регистрировать пользователя мы будем по первому сообщению:

@bot.message_handler(commands=["start"])
def handle_start(message: Message) -> None:
    user_id = message.from_user.id
    username = message.from_user.username
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name


    try:
        User.create(
            user_id=user_id,
            username=username,
            first_name=first_name,
            last_name=last_name,
        )
        bot.reply_to(message, "Добро пожаловать в менеджер задач!")
    except IntegrityError:
        bot.reply_to(message, f"Рад вас снова видеть, {first_name}!")


# Для более удобной работы нам понадобятся состояния:
class UserState(StatesGroup):
    new_task_title = State()
    new_task_due_date = State()
    tasks_make_done = State()

# Создадим обработчик команды /newtask:
@bot.message_handler(state="*", commands=["newtask"])
def handle_new_task(message: Message) -> None:
    user_id = message.from_user.id
    if User.get_or_none(User.user_id == user_id) is None:
        bot.reply_to(message, "Вы не зарегистрированы. Напишите /start")
        return


    bot.send_message(user_id, "Введите название задачи")
    bot.set_state(message.from_user.id, UserState.new_task_title)
    with bot.retrieve_data(message.from_user.id) as data:
        data["new_task"] = {"user_id": user_id}

# User.get_or_none вернёт нам модель пользователя либо None. Так мы проверяем, 
        # зарегистрирован пользователь или нет.
# В хранилище мы создаём словарь new_task и вносим туда ID пользователя. 
        # Далее предлагаем пользователю ввести название задачи.

# Обработчик названия задачи выглядит так:

@bot.message_handler(state=UserState.new_task_title)
def process_task_title(message: Message) -> None:
    with bot.retrieve_data(message.from_user.id) as data:
        data["new_task"]["title"] = message.text
    bot.send_message(message.from_user.id, "Введите дату (ДД.ММ.ГГГГ):")
    bot.set_state(message.from_user.id, UserState.new_task_due_date)

# Вносим название задачи в хранилище и переходим к вводу даты:
@bot.message_handler(state=UserState.new_task_due_date)
def process_task_due_date(message: Message) -> None:
    due_date_string = message.text
    try:
        due_date = datetime.datetime.strptime(due_date_string, DATE_FORMAT)
    except ValueError:
        bot.send_message(message.from_user.id, "Введите дату (ДД.ММ.ГГГГ):")
        return

    with bot.retrieve_data(message.from_user.id) as data:
        data["new_task"]["due_date"] = due_date

    new_task = Task(**data["new_task"])
    new_task.save()
    bot.send_message(message.from_user.id, f"Задача добавлена:\n{new_task}")
    bot.delete_state(message.from_user.id)

# Метод strptime конвертирует ввод пользователя в объект даты по заданному формату. 
    # Если возникнет ошибка конвертации (неверный формат), мы напишем пользователю 
    # сообщение о повторном вводе.
# У нас готовы все данные для создания задачи (user_id, title, due_date), 
    # поэтому мы можем её создать. Мы использовали конструкцию распаковки словаря:
# Task(**data["new_task"])
# Она эквивалентна следующей записи:
Task(
    user_id=data["new_task"]["user_id"], 
    title=data["new_task"]["title"],
    due_date=data["new_task"]["due_date"]
)

# Перейдём к разработке команды /tasks:
@bot.message_handler(state="*", commands=["tasks"])
def handle_tasks(message: Message) -> None:
    user_id = message.from_user.id
    user = User.get_or_none(User.user_id == user_id)
    if user is None:
        bot.reply_to(message, "Вы не зарегистрированы. Напишите /start")
        return

    tasks: List[Task] = user.tasks.order_by(-Task.due_date, -Task.task_id).limit(10)

    result = []
    result.extend(map(str, reversed(tasks)))

    if not result:
        bot.send_message(message.from_user.id, "У вас ещё нет задач")
        return

    result.append("\nВведите номер задачи, чтобы изменить её статус.")
    bot.send_message(message.from_user.id, "\n".join(result))
    bot.set_state(message.from_user.id, UserState.tasks_make_done)