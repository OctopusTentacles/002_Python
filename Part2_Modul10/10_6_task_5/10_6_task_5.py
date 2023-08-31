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


import os



# MAIN_CODE====================================================================

