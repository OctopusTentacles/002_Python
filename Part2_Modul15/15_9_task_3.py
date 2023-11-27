# Задача 3. Дата
# Реализуйте класс Date, который должен:

# проверять числа даты на корректность;
# конвертировать строку даты в объект класса Date, состоящий из соответствующих 
# числовых значений дня, месяца и года.
# Оба метода должны получать на вход строку вида ‘dd-mm-yyyy’.

# При тестировании программы объект класса Date должен инициализироваться 
# исключительно через метод конвертации, например:

# date = Date.from_string('10-12-2077')
# Неверный вариант: date = Date(10, 12, 2077)

# Результат:
# День: 10    Месяц: 12    Год: 2077
# True
# False

import datetime


class Date:


    def __init__(data_str) -> None:
        pass

    def is_date_valid(data_str):
        my_date = datetime.datetime.strptime(data_str, "%d-%m-%Y")
        if my_date:
            return True
        return False


    def from_string(data_str):
        my_date = datetime.datetime.strptime(data_str, "%d-%m-%Y")
        return f"День: {my_date.day}    Месяц: {my_date.month}    Год: {my_date.year}"


    pass



date = Date.from_string('10-12-2077')
print(date)
print(Date.is_date_valid('10-12-2077'))
print(Date.is_date_valid('40-12-2077'))
