import math
print('Задача 6. Ход конём')

# В рамках разработки шахматного ИИ стоит новая задача.
# По заданным вещественным координатам коня
# и второй точки программа должна определить может ли конь ходить в эту точку.
#
# Используйте как можно меньше конструкций if и логических операторов.
# Обеспечьте контроль ввода.

# Введите местоположение коня:
# 0.071
# 0.118
# Введите местоположение точки на доске:
# 0.213
# 0.068
# Конь в клетке (0, 1). Точка в клетке (2, 0).
# Да, конь может ходить в эту точку.

while True:
    print('Введите местоположение коня:')
    horseX = float(input())
    horseY = float(input())
    if (horseX < 0 or horseX > 0.79) or (horseY < 0 or horseY > 0.79):
        print('Проверьте местоположение коня\n')
        continue
    print('Введите местоположение точки на доске:')
    pointX = float(input())
    pointY = float(input())
    if (pointX < 0 or pointX > 0.79) or (pointY < 0 or pointY > 0.79):
        print('Такой координаты не существует\n')
        continue
    break

horseX_sq = int(horseX * 10)
horseY_sq = int(horseY * 10)
pointX_sq = int(pointX * 10)
pointY_sq = int(pointY * 10)

print(
    f'Конь в клетке ({horseX_sq}, {horseY_sq}). Точка в клетке ({pointX_sq}, {pointY_sq})')
if abs(horseX_sq - pointX_sq) == 2 and abs(horseY_sq - pointY_sq) == 1:
    print('Да, конь может ходить в эту точку.')
else:
    print('Конь так не ходит!')
