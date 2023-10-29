# Задача 1. Бесконечный генератор
# По аналогии с бесконечным итератором из практики предыдущего урока, 
# реализуйте свой счётчик-генератор, который также в цикле будет бесконечно 
# выдавать значения.

# Дополнительно: преобразуйте (или напишите с нуля) итератор 
# простых чисел в функцию-генератор.


def fibonacci(numbers):
    """fibonacci sequence"""
    cur_num = 0
    next_num = 1
    for _ in range(numbers):
        yield cur_num
        cur_num, next_num = next_num, cur_num + next_num
        if cur_num > 10 ** 6:
            return


fib_seq = fibonacci(100)
for seq in fib_seq:
    print(seq, end=" ")