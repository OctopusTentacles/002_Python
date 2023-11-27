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



# import datetime


# class Date:
#     def __init__(data_str) -> None:
#         pass

#     def is_date_valid(data_str):
#         try:
#             my_date = datetime.datetime.strptime(data_str, "%d-%m-%Y")
#             if my_date:
#                 return True
#             raise Exception
#         except Exception:
#             return False

#     def from_string(data_str):
#         my_date = datetime.datetime.strptime(data_str, "%d-%m-%Y")
#         return f"День: {my_date.day}    Месяц: {my_date.month}    Год: {my_date.year}"


class Date:

    def __init__(self, day, month, year) -> None:
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def is_date_valid(cls, data_str):
        try:
            day, month, year = map(int, data_str.split("-"))

            if (1 <= day <= 31) and (1 <= month <= 12):
                return True
            
            raise Exception
        except Exception:
            return False
        
    @classmethod
    def from_string(cls, data_str):
        if cls.is_date_valid(data_str):
            day, month, year = map(int, data_str.split("-"))
            return f"День: {day}    Месяц: {month}    Год: {year}"


date = Date.from_string('10-12-2077')
print(date)
print(Date.is_date_valid('10-12-2077'))
print(Date.is_date_valid('40-12-2077'))
