print('Задача 4. Отрезок')

# Напишите программу, которая считывает с клавиатуры три числа a, b и c,
# считает и выводит на консоль среднее арифметическое всех чисел
# из отрезка [a; b], кратных числу c.

numberA = int(input("Введите число а: "))
numberB = int(input("Введите число b: "))
numberC = int(input("Введите число c: "))
sumNumber = 0
count = 0
for i in range(numberA, numberB + 1, 1):
    if i // numberC == 0:
        print(i)
        sumNumber += i
        count += 1
print("среднее арифметическое всех чисел", sumNumber / count)
