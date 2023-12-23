# Что такое ORM

# Ранее мы рассмотрели взаимодействие с базой данных с помощью SQL-запросов. 
# У такого подхода есть большой минус — ненадёжность. Запросы получаются громоздкими, 
# и в них легко ошибиться. В результате исполнения запроса получаются кортежи, 
# поэтому можно прогадать с индексами.

# Эту проблему решает такая технология, как ORM (Object-Relational Mapping). 
# Она предоставляет удобный интерфейс, который связывает базу данных и объекты в коде.

# Например, в приложении приюта для домашних питомцев есть модель «Кот». 
# Она представлена как в базе данных:
# CREATE TABLE IF NOT EXISTS cats (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT,
#     age_months INTEGER
# );


# так и в самом приложении:
class Cat:
    id: int
    name: str
    age_months: int

# Какие действия мы совершаем, чтобы получить список котов?

# Делаем запрос в базу данных.
# Получаем список кортежей.
# Преобразуем список кортежей в список котов.
# По факту мы работаем с двумя моделями, которые идентичны по смыслу.

# При работе с ORM действия будут такими:

# Получаем список котов.
# Да, вот так всё просто.

# В Python существует множество ORM-библиотек. Некоторые из них:

# SQLAlchemy,
# Django ORM,
# Peewee,
# Pony ORM,
# Tortoise ORM,
# SQLObject.
    
# 