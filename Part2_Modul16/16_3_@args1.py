# Задача 1. Повторение кода
# В одной из практик вы уже писали декоратор do_twice, 
# который повторяет вызов декорируемой функции два раза. В этот раз 
# реализуйте декоратор repeat, который повторяет задекорированную 
# функцию уже n раз. 



def do_twise(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        return 
    return wrapper



def greeting(name: str) -> None:
    print('Привет, Tome!')
