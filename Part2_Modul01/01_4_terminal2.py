# Задача 2. Калькулятор
# Напишите программу калькулятор. Пользователь вводит два числа A и B и 
# действие X (плюс, минус, умножить, разделить). 
# Программа выводит результат в виде A X B = C, где C — результат этого 
# действия над числами A и B. Используйте только консоль и текстовый редактор. 
# Обеспечьте контроль ввода.

 
# Пример работы программы в консоли:
# Выберите операцию: +
# Введите первое число: 5
# Введите второе число: 6
# 5 + 6 = 11

 

# Пример работы программы в консоли 2:
# Выберите операцию: №
# Ошибка: такой операции не существует. Попробуйте ещё раз.
# Выберите операцию: -
# Введите первое число: 5
# Введите второе число: 6
# 5 - 6 = -1

while True:
    operation = input('Выберите операцию: ')
    if operation in '+-*/':
        break
    print('Ошибка: такой операции не существует. Попробуйте ещё раз.')
        
number1 = int(input('Введите первое число: '))
number2 = int(input('Введите второе число: '))

if operation == '+':
    result = number1 + number2
elif operation == '-':
    result = number1 - number2
elif operation == '*':
    result = number1 * number2
elif operation == '/':
    result = number1 / number2

print(number1, operation, number2, '=', result)


    