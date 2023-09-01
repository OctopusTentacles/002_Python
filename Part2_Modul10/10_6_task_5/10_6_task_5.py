# Задача 05. Надёжные вычисления
# Контекст
# Вы работаете в компании, занимающейся финансовыми вычислениями. 
# Вам необходимо разработать функцию для вычисления квадратного корня числа, 
# которая будет использоваться в анализе финансовых данных и расчёте 
# инвестиционных показателей. Вы понимаете, что передача отрицательного числа 
# или возникновение других ошибок вычисления могут привести 
# к непредсказуемым результатам.

# Задача
# Напишите функцию, которая будет:
# Вычислять и возвращать квадратный корень полученного числа.
# Обрабатывать исключения для отрицательных чисел и других возможных ошибок.

# Советы
# При помощи оператора as вы можете сохранить пойманную ошибку в переменную, 
# чтобы затем использовать её для получения дополнительной информации:
# except Exception as exc:
#     print(exc)
# Старайтесь не смешивать конкретные исключения, которые вы ожидаете, 
# со всеми другими (except Exception будет ловить все исключения, 
# которые не были пойманы предыдущими except).


import math


# def square_num(num):
#     try:
#         if num == 0:
#             raise Exception('0 всегда 0')
                
#         sqrt_num = math.sqrt(num)
#         return sqrt_num
    
#     except ValueError:
#         return('не может быть найден так как число отрицательное')

#     except Exception as exc:
#         return exc


# # MAIN_CODE====================================================================

# for _ in range(6):
#     try:
#         number = float(input('Введите число: '))
#         if isinstance(number, str):
#             raise Exception

#         sqrt_number = square_num(number)

#         print(f'квадратный корень числа: {sqrt_number}')
#     except Exception:
#         print('Вы ввели не число, повторите ввод')


def get_sage_sqrt(num):
    try:
        if num == 0:
            raise Exception('0 всегда 0')

        if isinstance(num, str):
            raise Exception('Вы ввели не число, повторите ввод')

        sqrt_num = math.sqrt(num)
        if isinstance(num, float):
            raise Exception(round(sqrt_num, 1))
        return sqrt_num

    except ValueError:
        return 'не может быть найден так как число отрицательное'

    except Exception as exc:
        return exc


# Тестовые случаи
numbers = [16, 25, -9, 0, 4.5, "abc"]
for number in numbers:
    result = get_sage_sqrt(number)
    print(f"Квадратный корень numbers {number}: {result}")