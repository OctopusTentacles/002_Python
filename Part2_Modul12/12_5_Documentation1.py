# docstring

class Person:
    """ 
    Базовый класс, описывающий человека 
    
    __count: общее количество человек

    Args:
        name (str): передается имя человека
        age (int): передается возраст человека

    Attributes:
        max_count (int): максимальное количество инстансов

    """
    __count = 0
    max_count = 5

    def __init__(self, name, age):
        self.__name = name
        self.set_age(age)
        self.__location = "Moscow"

        if Person.__count > self.max_count:
            raise Exception("Слишком много людей")
        Person.__count += 1

    def get_age(self):
        """
        Геттер для получения возраста

        :return: __age
        :rtype: int

        """
        return self.__age
    
    def set_age(self, age):
        """
        Сеттер для установления возраста

        :param age: возраст
        :raise Exception: если возраст не в границах от1 до 90, то 
                вызывается исключение
        """
        if age in range(1, 90):
            self.__age = age
        else:
            raise Exception("Недопустимый возраст")


class Employee(Person):
    """
    Класс работник. Родитель: Person

    Args:
        name (str): передается имя человека
        age (int): передается возраст человека

    Attributes:
        max_count (int): максимальное количество инстансов
        job (str): Должность работника
    """
    def __init__(self):
        super().__init__()
        self.job = 'Sales Manager'

    def get_job(self):
        return self.job
    
    def employ(self, value):
        self.job = value
        if value is None:
            self.job = "unemployed"


print(Person.__doc__)