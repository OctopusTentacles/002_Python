# Задача 2. Сортировка
# Таблица базы данных состоит из строк, в которых хранится информация о каждом человеке: 
# его имя, возраст и остальные данные. Вас попросили реализовать для этой базы 
# сортировку по возрасту (по убыванию и по возрастанию). 

# Реализуйте класс Person с соответствующей инициализацией, 
# а также сеттерами и геттерами. Затем создайте список из хотя бы трёх людей и 
# отсортируйте их. Для сортировки используйте лямбда-функцию.


class Person:

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name
      
    @name.setter
    def name(self, name):
        self._name = name
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, age):
        self._age = age

    def __repr__(self) -> str:
        return f"({self.name}, {self.age})"


person_1 = Person('Tom', 35)
person_2 = Person('Tim', 12)
person_3 = Person('Ben', 99)
person_list = [person_1, person_2, person_3]
print(person_list)

sorted_person = sorted(person_list, key=lambda elem: elem.age)
print(sorted_person)
sorted_person = sorted(person_list, key=lambda elem: -elem.age)
print(sorted_person)

person_list.sort(key=lambda elem: elem.age)
print(person_list)
person_list.sort(key=lambda elem: -elem.age)
print(person_list)