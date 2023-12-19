# SQLite

# База данных — совокупность данных, которые хранятся в соответствии с заданной схемой.

# SQLite — система управления базами данных (СУБД), которые основаны на отношениях 
# сущностей. Такие БД называются реляционными (от англ. relation — отношение).

# Lite в названии действительно означает лёгкость в использовании. 
# Если в таких гигантах, как PostgreSQL или MySQL, для содержания БД поднимается 
# отдельный сервер, то SQLite создаёт лишь один файл, с которым и работает. 
# Также её довольно легко настраивать (по сути, это даже не требуется), 
# поэтому с неё мы и начнём наш путь знакомства с базами данных.

# Итак, набираем в командной строке:
# sqlite3

# Видим, что сейчас мы не привязаны к какому-то файлу. 
# Давайте с помощью предложенной команды создадим его:
# sqlite> .open database.db

# Либо можно сразу создать базу данных, указав её название при запуске:
# sqlite3 database.db

# Написав .help, можно увидеть доступные команды:
# sqlite> .help


# Создание таблицы
# Наша таблица будет называться students, в ней мы будем хранить информацию 
# о студентах — их id, имена и фамилии.
# sqlite> CREATE TABLE students(
#    ...>   id INTEGER PRIMARY KEY AUTOINCREMENT,
#    ...>   name TEXT NOT NULL,
#    ...>   surname TEXT NOT NULL
#    ...> );
# INTEGER — целочисленный тип данных.
# TEXT — строковый тип данных.
# NOT NULL означает, что поле не может быть пустым.
# PRIMARY KEY говорит, что этот ключ будет первичным, — 
# его значения будут уникальными для всей таблицы.
# AUTOINCREMENT означает, что при создании нового студента его id будет 
# увеличен на 1 относительно последнего.

# Создание записи
# Для создания записи мы используем оператор INSERT:

# sqlite> INSERT INTO students (name, surname) VALUES ('Иван', 'Иванов');
# sqlite> INSERT INTO students (name, surname) VALUES ('Петр', 'Петров');
# sqlite> INSERT INTO students (name, surname) VALUES ('Анна', 'Аннова');
# В первых скобках указываются поля, которые мы добавляем; 
# в соответствии с ними во вторых скобках — значения для вставки. 
# Здесь мы не указываем id — он будет вычисляться автоматически.

# Так-с, добавили. А как посмотреть?
# Чтение записей
# Для просмотра записей мы используем оператор SELECT:
# sqlite> SELECT * FROM students;
# 1|Иван|Иванов
# 2|Петр|Петров
# 3|Анна|Аннова
# Звёздочка * говорит, что нам нужно получить все поля из таблицы students. 

# Добавим немного красоты при выводе, исполнив следующие две команды:
# sqlite> .headers on
# sqlite> .mode box

# Сделаем запрос посложнее. Выберем студентов с id > 1 и получим только 
# поля id и surname:
# sqlite> SELECT id, surname FROM students WHERE id > 1;

# Если мы хотим более сложное условие, можно использовать операторы AND или OR:
# SELECT id, surname FROM students WHERE id > 1 AND surname like '%ова';
# Так мы получим всех студентов с фамилией на -ова и id > 1.
# Знак процента говорит о том, что перед окончанием «ова» есть какие-то символы.