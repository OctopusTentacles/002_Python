# Задача 1. Матрица

# Дан вот такой список со списками:
# Реализуйте программу, которая выводит элементы этого списка 
# в виде привычной нам матрицы.

# Результат работы программы:
# 1 2 3
# 4 5 6
# 7 8 9

matrix = [[1, 2 ,3], [4, 5, 6], [7, 8, 9]]

for i_matrix in matrix:
    for i_num in i_matrix:
        print(i_num, end=' ')
    print()