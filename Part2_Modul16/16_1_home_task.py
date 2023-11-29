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
    
    


# MAIN CODE:==========================================================================
date = Date.from_string('10-12-2077')
print(date)
print(Date.is_date_valid('10-12-2077'))
print(Date.is_date_valid('40-12-2077'))
