# Задача 1. Бесконечный генератор
# По аналогии с бесконечным итератором из практики предыдущего урока, 
# реализуйте свой счётчик-генератор, который также в цикле будет бесконечно 
# выдавать значения.

# Дополнительно: преобразуйте (или напишите с нуля) итератор 
# простых чисел в функцию-генератор.


def fibonacci(numbers):
    """ fibonacci sequence """
    cur_num = 0
    next_num = 1
    for _ in range(numbers):
        yield cur_num
        cur_num, next_num = next_num, cur_num + next_num
        if cur_num > 10 ** 6:
            return

def square(numbers):
    """ Fibonacci sequence squared """
    for num in numbers:
        yield num ** 2

fib_seq = fibonacci(10)
for seq in fib_seq:
    print(seq, end=" ")

print()

# генератор от генератора
print(sum(square(fibonacci(10))))

# генераторные выражения
print((i ** 3 for i in range(10)))

cubes_gen = (i ** 3 for i in range(10))
for cube in cubes_gen:
    print(cube, end=" ")
print()
print("=" * 90, end="")
# =============================================================================
print()

def endless(count=2):
    """ Infinite generator """
    while True:
        yield count
        count += 1

# преобразуйте итератор простых чисел в функцию-генератор:
def simpleGen():
    """ Simple numbers generator """
    list_num = []
    my_gen = endless()
    for i_elem in my_gen:
        for number in list_num:
            if i_elem % number == 0:
                break
        else:
            list_num.append(i_elem)
            yield i_elem


# 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47
prime_nums = simpleGen()
for i_elem in prime_nums:
    print(i_elem, end=' ')
