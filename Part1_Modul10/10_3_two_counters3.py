# Задача 3. Диагональная матрица

# Напишите программу, которая получает на вход размер квадратной матрицы
# и выводит на экран по такому принципу диагональ из единиц с левого
# нижнего угла до верхнего правого, ниже диагонали — двойки, выше — нули.

size = int(input('Введите размер квадратной матрицы: '))

for row in range(size):
    for col in range(size):
        if -row + (size - 1) == col:
            print(1, end=' ')
        elif -row + (size - 1) < col:
            print(2, end=' ')
        else:
            print(0, end=' ')
    print()
