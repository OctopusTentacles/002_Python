# Задача 2. Плагины
# Один проект состоит из огромного количества разнообразных функций, 
# часть из которых используется в других проектах в качестве плагинов, 
# то есть они как бы «подключаются» и создают дополнительный функционал.

# Реализуйте специальный декоратор, который будет «регистрировать» нужные 
# функции как плагины и заносить их в соответствующий словарь. 

from typing import Callable, Any, Dict


plugins: Dict[str, Callable] = dict()

def register(func: Callable) -> Callable:
  """ Декоратор регистрирует функцию как плагин """
    

@register
def hello(name: str) -> str:
   print("Hello {name}!".format(name=name))

@register
def goodbye(name: str) -> str:
   print("Goodbye {name}!".format(name=name))


print(plugins)