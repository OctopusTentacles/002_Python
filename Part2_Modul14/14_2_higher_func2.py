# Задача 2. Таймер
# Вы работаете в отделе тестирования, и вам поручили с помощью различных функций замерить 
# скорость передачи данных на нескольких десятках сайтов. Конечно же, вручную «щёлкать» 
# сайты и замерять время вам было лень, поэтому возникла идея написать «автотест», 
# который всё сделает сам.

# С помощью понятия функции высшего порядка реализуйте функцию-таймер, 
# которая замеряет время работы переданной функции func и выдаёт ответ на экран.

# Проверьте работу таймера на какой-нибудь «тяжеловесной» функции.


import time
from typing import Callable, Any

def timer(func: Callable) -> Any:
    start = time.time()
    func()
    stop = time.time()
    return stop - start

def hard_func():
    pass


print(timer(hard_func))