# Задание 1. Дом для семьи
# Максим написал программу, которая должна определять, подходит ли 
# земельный участок для его семьи или нет. Живут они втроем, вот и 
# условие будет таким же: если количество квадратных метров делится 
# на 3, то участок подходит.

# Скопируйте программу в редактор и исправьте её. 
# Убедитесь, что она работает правильно и решает задачу Максима.

for meters in  100,90,95,87,102:
    if meters % 3 == 0:
        print(meters, 'Подходит')
    else:
        print(meters, 'Не подходит')