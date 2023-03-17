# couple of letters

string = input("Введите строку: ")  # abc / abbc
prevSym = ""
equalSym = False
for symbol in string:
    if prevSym == symbol:
        equalSym = True
        break
    else:
        prevSym = symbol

if equalSym:
    print("Есть две одинаковые буквы подряд")
else:
    print("Нет двух одинаковых букв подряд")
