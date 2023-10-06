# Задача 3. Кастомные исключения
# Исключения в Python также являются классами, и все они берут свои истоки 
# от самого главного класса — Exception. И для создания своего собственного 
# класса ошибки достаточно написать его дочерний класс. Например:

# class MyOwnException(Exception):
#     pass
# raise MyOwnException('Это моя ошибка!')

# Причём содержимое объекта исключения чаще всего так и оставляют (просто pass), 
# чтобы не сломать автоматические обработчики исключений.

# Напишите программу, которая считывает из файла numbers.txt пары чисел, 
# делит первое число на второе и выводит ответ на экран. 
# Если первое число меньше второго, то программа выдаёт исключение DivisionError 
# (нельзя делить меньшее на большее). 

# Дополнительно, с помощью try except, можно обработать исключение на своё усмотрение.


class DivisionError(Exception):
    pass


with open("numbers.txt", "r", encoding="utf8") as file:
    for line in file:
        try:
            clear_line = line.strip()
            first, second = clear_line.split()
            if int(first) < int(second):
                raise DivisionError("нельзя делить меньшее на большее")
        except (ValueError, DivisionError) as exc:
            print(exc, type(exc), first, second)
