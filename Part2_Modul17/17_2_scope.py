# Задача 1. Счётчик 2
# Как-то мы уже создавали декоратор counter, который считает и выводит 
# количество вызовов декорируемой функции. Для этого мы использовали интересную 
# особенность классов. В этот раз реализуйте тот же декоратор, 
# но уже с использованием знаний о локальных и глобальных переменных.

# Реализуйте декоратор двумя способами: 
# используя глобальную переменную count; 
# используя локальную переменную count внутри декоратора.

# Дополнительно: найдите команду (в интернете или даже сами), 
# которая перечисляет все функции и методы, находящиеся во встроенном 
# пространстве имён в Python.


global_count = {}

def decorator_counter(func):
    local_count = {}

    def wrapper(*args, **kwargs):
        
        global_count[func.__name__] = global_count.get(func.__name__, 0) + 1
        local_count[func.__name__] = local_count.get(func.__name__, 0) + 1
        
        print(global_count, local_count)
        return func(*args, **kwargs)
    return wrapper




@decorator_counter
def example_1():
    print("Hello!")


example_1()



# Результат выполнения команды:
# ['__class__', '__class_getitem__', '__contains__', '__delattr__', 
#  '__delitem__', '__dir__'  ну и так далее.