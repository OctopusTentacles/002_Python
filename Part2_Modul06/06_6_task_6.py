# Задача 6. Пицца

# В базе данных интернет-магазина PizzaTime хранятся данные о том, кто, 
# что и сколько заказывал у них в определённый период. 
# Вам нужно структурировать эту информацию, а также понять, 
# сколько всего пицц купил каждый заказчик.

# На вход в программу подаётся N заказов. Каждый заказ представляет 
# собой строку вида 
# «Покупатель — название пиццы — количество заказанных пицц». 
# Реализуйте код, который выводит список покупателей и их заказов по алфавиту. 
# Учитывайте, что один человек может заказать одно и то же несколько раз.

# Пример:
# Введите количество заказов: 6
# Первый заказ: Иванов Пепперони 1
# Второй заказ: Петров Де-Люкс 2
# Третий заказ: Иванов Мясная 3
# Четвёртый заказ: Иванов Мексиканская 2
# Пятый заказ: Иванов Пепперони 2
# Шестой заказ: Петров Интересная 5

# Иванов: 
#      Мексиканская: 2
#      Мясная: 3
# 	   Пепперони: 3
# Петров:
# 	   Де-Люкс: 2
# 	   Интересная: 5

client_data = dict()

for order in range(1, int(input('Введите количество заказов: ')) + 1):
    client_list = input(f'{order} заказ: ').title().split(' ')

    client_data.setdefault(client_list[0], {})
    client_data[client_list[0]].setdefault(client_list[1], [])
    client_data[client_list[0]][client_list[1]].append(client_list[2])

print(client_data)

for client in sorted(client_data):
    print(f'{client}:')

    for pizza in sorted(client_data[client]):
        print(f'     {pizza}: {sum(map(int, client_data[client][pizza]))}')

# Тут функция map применяет функцию int к каждому элементу объекта