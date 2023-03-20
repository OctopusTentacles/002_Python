# Задача 1. Таблица умножения

# Математик Паша недавно заметил, что у него уже есть куча разных таблиц степеней,
# но нет самого основного — таблицы умножения. Пора бы это исправить.

# Напишите программу, которая выводит таблицу умножения для чисел от 1 до 9.
# Для этого используйте конструкцию вложенного цикла: внешний отвечает
# за первый множитель, а внутренний — за второй.

# Дополнение: выведите настоящую таблицу умножения, без всяких знаков,
# только числа. Чтобы она получилась красивой и ровной,
# используйте литерал \t внутри оператора end. \t — это литерал табуляции,
# благодаря ему все числа выстраиваются в виде таблицы. Результат должен получиться таким:

for x in range(1, 10):
    for y in range(1, 10):
        print(x * y, end="\t")
    print()
