print('Задача 5. Маятник ')

# Известно, что амплитуда качающегося маятника с каждым разом затухает
# на 8,4% от амплитуды прошлого колебания.
# Если качнуть маятник,
# то, строго говоря, он не остановится никогда,
# просто амплитуда будет постоянно уменьшаться до тех пор,
# пока мы не сочтём такой маятник остановившимся.

# Напишите программу,
# определяющую, сколько раз качнётся маятник, прежде чем он, по нашему мнению, остановится.

# Программа получает на вход
# начальную амплитуду колебания в сантиметрах
# и конечную амплитуду его колебаний,
# которая считается остановкой маятника.

# Обеспечьте контроль ввода.

# Пример:

# Введите начальную амплитуду: 1
# Введите амплитуду остановки: 0.1

# Маятник считается остановившимся через 27 колебаний


def damping(a, b):
    swaying = 0
    while a > b:
        a = a - (a * 8.4 / 100)
        swaying += 1
    return swaying


while True:
    start = float(input('\nВведите начальную амплитуду: '))
    stop = float(input('Введите амплитуду остановки: '))
    if (start < 0 or start < stop) or stop < 0:
        print('Ошибка ввода.')
    else:
        break
print(
    f'Маятник считается остановившимся через {damping(start, stop)} колебаний')
