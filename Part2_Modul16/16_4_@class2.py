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

def logging(func, class_name):
    def wrapper(*args, **kwargs):
        print(func(*args, **kwargs))

        print(f"Класс: {class_name} Функция: {func.__name__} \
              произошёл в:", datetime.datetime.now())
        
        
    return wrapper

def decorator(cls):
        for i_def in dir(cls):
            if i_def.startswith('__') is False:
                cur_meth = getattr(cls, i_def)
                if hasattr(cur_meth, '__call__'):
                    
                    decorated = logging(cur_meth, cls.__name__)
                    setattr(cls, i_def, decorated)
            
        return cls

@decorator
class MyClass:
    # @logging
    def method_1(self) -> None:
        return ("a")

    # @logging
    def method_2(self) -> None:
        return ("b")

    # @logging
    def method_3(self) -> None:
        return ("c")

MyClass().method_1()
MyClass().method_2()
MyClass().method_3()