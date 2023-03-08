number = int(input("Введите число: "))
isPrime = True
for devider in range(2, number):
    if number % devider == 0:
        isPrime = False
        break
if isPrime:
    print("Число простое")
else:
    print("Число составное")