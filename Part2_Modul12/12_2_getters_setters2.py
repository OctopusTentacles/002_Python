# Задача 2. Человек
# Реализуйте класс «Человек», который инициализируется именем 
# (имя должно состоять только из букв) 
# и возрастом (должен быть в диапазоне от 0 до 100), а внутри класса 
# считается общее количество инициализированных объектов. 
# Реализуйте сокрытие данных для всех атрибутов (как статических, так и динамических), 
# а для изменения и получения данных объекта 
# напишите специальные геттеры и сеттеры. 

# При тестировании класса измените приватный атрибут (например, возраст) 
# двумя способами: сеттером и «крайне не рекомендуемым», который был показан в уроке.


class Human:
    __count = 0

    def __init__(self, name, age):
        self.__name = ''
        self.__age = 0
        self.set_age(age)
        self.set_name(name)

        Human.__count += 1

    def __str__(self):
        return f'Имя: {self.__name}, возраст: {self.__age} '
    
    def get_count(self): # геттер
        return self.__count

    def get_age(self): # геттер
        return f'возраст {self.__name} - {self.__age}'
    
    def set_name(self, name): # сеттер
        if isinstance(name, str) and name.isalpha():
            self.__name = name
        else:
            raise Exception('Ошибка в имени!')

    def set_age(self, age): # сеттер
        if isinstance(age, (int, float)) and age in range(0, 101):
            self.__age = age
        else:
            raise Exception('Недопустимый возраст!')


mike = Human('Mike', 40)
alice = Human('Alice', 4)

print(mike)
print(alice)

mike.set_name('fuck')
mike.set_age(45)

print(mike.get_age())
print(alice.get_count())
# ====================================================================
print(Human._Human__count)