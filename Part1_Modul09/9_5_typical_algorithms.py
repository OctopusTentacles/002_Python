# filter

text = input("Введите текст: ")
summ = 0
print("\nОтфильтрованный текст: ", end="")
for symbol in text:
    if symbol == "1" or symbol == "9":
        summ += int(symbol)
    else:
        print(symbol, end="")
print("\nСумма:", summ)
