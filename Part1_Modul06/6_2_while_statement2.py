# Напишите программу, которая спрашивает у пользователя 
# «Сколько отложить денег?» до тех пор, пока сумма в копилке 
# не превысит или не станет равна 500 000 рублей.

balance = int(input("Сколько отложить денег? "))
while balance < 500000:
    moneybox = int(input("Сколько отложить денег? "))
    balance += moneybox
print("Вы накопили", balance )
