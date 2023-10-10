# Задача 3. Свой словарь
# Что нужно сделать
# В силу обстоятельств Васе постоянно приходится работать со словарями и их данными. 
# В том числе и с методом get, который по умолчанию возвращает None, если такого ключа 
# в словаре нет. Однако Васю это не устраивает: 
# для нормальной работы ему нужно возвращать число 0.

# Реализуйте класс MyDict, который будет вести себя точно так же, 
# как и обычный словарь (попробуйте унаследовать его от оригинального dict), 
# за исключением того, что метод get по умолчанию будет возвращать не None, а число 0.



# dict = {"key_1": value, number: value}
# get(key[, default])
print(dict.__doc__)


class MyDict(dict):

    def get(self, key):
        self.key = key
        if not self.key:
            return 0
        return value
    

my_dict = {"one": 1, "two": 2, "three": 3, "four": 4}
print(my_dict.get("two"))
print(my_dict.get("five"))

my_dict_1 = MyDict(my_dict)
print(my_dict_1.get("two"))
print(my_dict_1.get("five"))
