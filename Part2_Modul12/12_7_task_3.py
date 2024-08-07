# Задача 3. Свой словарь
# Что нужно сделать
# В силу обстоятельств Васе постоянно приходится работать со словарями и их данными. 
# В том числе и с методом get, который по умолчанию возвращает None, если такого ключа 
# в словаре нет. Однако Васю это не устраивает: 
# для нормальной работы ему нужно возвращать число 0.

# Реализуйте класс MyDict, который будет вести себя точно так же, 
# как и обычный словарь (попробуйте унаследовать его от оригинального dict), 
# за исключением того, что метод get по умолчанию будет возвращать не None, а число 0.


"""некоторые заметки, чтобы разобраться и понять"""
# dict = {"key_1": value, number: value}
# get(key[, default]), default = None
# get(key, None) - get(key, 0)
# print(dict.__doc__)


class MyDict(dict):
    """ дочерний класс MyDict от класса dict
        все атрибуты и методы наследуются от родителя 
    """
    def get(self, key, default=0):
        """ метод get() переопределен,
            значение default = None на значение 0
            при отсутствии ключа вместо None получаем 0
        """
        return super().get(key, default)

"""тестирование стандартного class dict"""
my_dict = {"one": 1, "two": 2, "three": 3}
print(my_dict.get("two"))
print(my_dict.get("five"))

"""тестирование нашего class MyDict"""
my_dict_1 = MyDict(my_dict)
print(my_dict_1.get("three"))
print(my_dict_1.get("five"))
