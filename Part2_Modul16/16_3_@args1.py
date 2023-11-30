# Задача 1. Повторение кода
# В одной из практик вы уже писали декоратор do_twice, 
# который повторяет вызов декорируемой функции два раза. В этот раз 
# реализуйте декоратор repeat, который повторяет задекорированную 
# функцию уже n раз. 


def repeat(qnt: int):
    def do_twise(func):
        def wrapper(*args, **kwargs):
            for _ in range(qnt):
                func(*args, **kwargs)
            return 
        return wrapper
    return do_twise


@repeat(5)
def greeting(name: str) -> None:
    print('Привет, {name}!'.format(name = name))

greeting("Tom")