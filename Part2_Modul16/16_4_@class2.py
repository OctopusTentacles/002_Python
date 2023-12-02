# Задача 2. Декорацию знаешь?
# На новой работе вы познакомились с middle-разработчиком на Python, 
# который согласился научить вас всему, что умеет сам. 
# Но перед этим он решил точечно проверить ваши знания. Он показал код, 
# где один и тот же декоратор логирования использовался для каждого метода 
# класса отдельно:

# Зная, что классы тоже можно декорировать, вы сразу поняли, 
# как можно упростить код.

# Реализуйте декоратор logging, который должен декорировать класс и логировать 
# каждый метод в нём. Логирование реализуйте на своё усмотрение: 

# это может быть, например, вывод названия метода, его аргов, кваргов и 
# документации на экран;
# либо вывод всей этой информации в отдельный файл вместе с датой и временем.


import datetime

def logging(func):
    def wrapper(*args, **kwargs):
        print("Запуск функции произошёл в:", datetime.datetime.now())
        return func(*args, **kwargs)
    return wrapper

def decorator(cls):
        for i_method in dir(cls):
            if i_method.startswith('__') is False:
                cur_meth = getattr(cls, i_method)
                if hasattr(cur_meth, '__call__'):
                     decorated = logging(cur_meth)
                     setattr(cls, i_method, decorated)
            
        return cls


class MyClass:
    @logging
    def method_1(self) -> None:...

    @logging
    def method_2(self) -> None:...

    @logging
    def method_3(self) -> None:...
