# Задача 1. Двойной вызов
# Реализуйте декоратор do_twice, который дважды вызывает декорируемую функцию. 
# Не забывайте про документацию и аннотации типов.

# Пример декорируемой функции:
# def greeting(name):
#     print('Привет, {name}!'.format(name=name))

# Основной код:
# greeting('Tom')
# Результат:
# Привет, Tom!
# Привет, Tom!

# Шаблон 
# def decorator(func):
#   def wrapped_func(*args, **kwargs):
        # код вызова функции
#       value = func(*args, **kwargs)
        # код после вызова функции
#       return value
#   return wrapped_func

# @decorator


def greeting(name):
    print('Привет, {name}!'.format(name=name))
