class Person:
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
        return self.__age
    
    def set_age(self, age):
        if age in range(1, 90):
            self.__age = age
        else:
            raise Exception("Недопустимый возраст")


class Employee(Person):