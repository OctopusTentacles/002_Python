# Задача 3. Лестница чисел

# Пользователь вводит число N.
# Напишите программу, которая по этому числу
# выводит вот такую лестницу из чисел:

n = int(input('Введите число: '))
for row in range(n + 1):
    for col in range(row, n + 1):
        print(col, end=' ')
    print()
