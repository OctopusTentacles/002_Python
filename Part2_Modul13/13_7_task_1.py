# Задача 1. Квадраты чисел
# Что нужно сделать
# Пользователь вводит число N. Напишите программу, которая генерирует последовательность 
# из квадратов чисел от 1 до N (1 ** 2, 2 ** 2, 3 ** 2 и так далее). 
# Реализацию напишите тремя способами: 
# класс-итератор, функция-генератор и генераторное выражение.

# Есть аннотация типов для методов/функций и их аргументов (кроме args и kwargs). 
# Если функция/метод ничего не возвращает, то используется None.


class Iterator:
    """ class Iterator - генерирует последовательность из квадратов чисел от 1 до stop.
    """
    def __init__(self, stop: int) -> None:
        """ self.stop - число последней итерации. 
            self.num - число, возводимое в квадрат.
        """
        self.stop = stop
        self.num = 1

    def __iter__(self):
        return self
    
    def __next__(self) -> int:
        if self.num > self.stop:
            raise StopIteration
        sq_num = self.num ** 2
        self.num += 1
        return sq_num
    


number = int(input("Введите число: "))

print("\n1. class Iterator:")
sq_num = Iterator(number)
for num in sq_num:
    print(num, end=" ")