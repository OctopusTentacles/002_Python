# Задача 2. Плагины
# Один проект состоит из огромного количества разнообразных функций, 
# часть из которых используется в других проектах в качестве плагинов, 
# то есть они как бы «подключаются» и создают дополнительный функционал.

# Реализуйте специальный декоратор, который будет «регистрировать» нужные 
# функции как плагины и заносить их в соответствующий словарь. 

from typing import Callable, Any


plugins = dict()

def to_plugins(func):
  def wrapped_func(*args, **kwargs):
      value = func(*args, **kwargs)
      return value
  return wrapped_func


@to_plugins
def hello(name: str) -> str:
   print("Hello {name}!".format(name=name))

print(plugins)