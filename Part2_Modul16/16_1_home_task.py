# Реализуйте класс Date, который должен:

# проверять числа даты на корректность;
# конвертировать строку даты в объект класса Date, состоящий из соответствующих 
# числовых значений дня, месяца и года.
# Оба метода должны получать на вход строку вида ‘dd-mm-yyyy’.


class Date:
    """
    Класс для проверки и преобразования даты.
    """
    def __init__(self, day: int, month: int, year: int) -> None:
        self.day = day
        self.month = month
        self.year = year

    def __str__(self) -> str:
        return "День: {}\tМесяц: {}\tГод: {}".format(
            self.day, self.month, self.year
        )
    
    @classmethod
    def is_date_valid(cls, date: str) -> bool:
        day, month, year = map(int, date.split("-"))
        return 0 < day < 32 and 0 < month < 13 and 0 < year < 10000
    
    @classmethod
    def from_string(cls, date: str) -> 'Date':
        day, month, year = map(int, date.split("-"))
        return cls(day, month, year)

# MAIN CODE:==========================================================================
date = Date.from_string('10-12-2077')
print(date)
print(Date.is_date_valid('10-12-2077'))
print(Date.is_date_valid('40-12-2077'))
