# Задача 1. Урок литературы

# К уроку литературы нужно было прочитать “Евгения Онегина”.
# Учитель задаёт вопрос пяти случайным детям. Она задаёт вопрос
# “Кто написал произведение?” и если ученик не угадывает, то учитель
# ставит двойку и спрашивает следующего. Если хоть кто-то угадает,
# то вопросы больше не задаются. Напишите программу, которая
# посчитает количество двоечников из этих пяти.

badStudent = 0
for i in range(5):
    question = input("Кто написал произведение? ")
    if question == "Пушкин" or question == "пушкин":
        print("Молодец")
        break
    print("Неправильно, два!")
    badStudent += 1
print("Количество двоек", badStudent)
