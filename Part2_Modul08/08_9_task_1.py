# Задача 1. Challenge-2
# Что нужно сделать
# Вдохновившись мотивацией Антона, ваш друг тоже решил поставить перед собой 
# задачу, но не напрямую связанную с математикой, а именно: написать функцию, 
# которая выводит все числа от 1 до num без использования циклов. 
# Помогите другу реализовать такую функцию.

# Пример работы программы
# Введите num: 10
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10


def numbers(number):
    if number == 0:
        # return 1
        return
    numbers(number - 1)
    print(number)


num = int(input('Введите num: '))
numbers(num)

# рекурсия напрягает мой мозг знатно ))))))))))))))
# поставил при 0 возврат 1, но 1 получается возвращается в никуда - 
# возврат идет на number(1) и уже вывод
# вроде понятно, но не могу разложить по полочкам в голове))))