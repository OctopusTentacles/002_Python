# Задание 3. Товары

# В базе данных магазина вся необходимая информация 
# по товарам делится на два словаря: первый отвечает за коды товаров, 
# второй — за списки количества разнообразных товаров на складе:

# Каждая запись второго словаря отображает, сколько и по какой цене 
# закупалось товаров. Цена указана за одну штуку.

# Напишите программу, которая рассчитывает общую стоимость позиций 
# для каждого товара на складе и выводит эту информацию на экран.

# Результат работы программы:
# Лампа — 27 штук, стоимость 1134 рубля.
# Стол — 54 штуки, стоимость 27 860 рублей.
# Диван — 3 штуки, стоимость 3550 рублей.
# Стул — 105 штук, стоимость 10 311 рублей.


def word_money(price):
    if 5 <= price <= 20 or 5 <= price % 100 <= 20:
        return 'рублей'
    elif price % 10 == 1:
        return 'рубль'
    elif price % 10 in (2, 3, 4):
        return 'рубля'
    else:
        return 'рублей'
    
def word_quantity(quantity):
    if 5 <= quantity <= 20 or 5 <= quantity % 100 <= 20:
        return 'штук'
    elif quantity % 10 == 1:
        return 'штука'
    elif quantity % 10 in (2, 3, 4):
        return 'штуки'
    else:
        return 'штук'



goods = {'Лампа': '12345', 
         'Стол': '23456', 
         'Диван': '34567', 
         'Стул': '45678',
}

store = {'12345': [{'quantity': 27, 'price': 42},],
         '23456': [{'quantity': 22, 'price': 510},
                   {'quantity': 32, 'price': 520},],
         '34567': [{'quantity': 2, 'price': 1200},
                   {'quantity': 1, 'price': 1150},],
         '45678': [{'quantity': 50, 'price': 100},
                   {'quantity': 12, 'price': 95},
                   {'quantity': 43, 'price': 97},],
}
# ___________________________________________________________________________
# for item in goods:
#     total_qnty = 0
#     total_price = 0
#     for index in store[goods[item]]:
#         total_qnty += index.get('quantity')
#         total_price += index.get('price') * index.get('quantity')
#     print(f'{item} - {total_qnty} стоимость {total_price}')
# ____________________________________________________________________________

for item in goods:
    total_qnty = [index.get('quantity') for index in store[goods[item]]]
    total_price = [index.get('price') * index.get('quantity') 
                   for index in store[goods[item]]]
    
    print(f'{item} - {sum(total_qnty)} {word_quantity(sum(total_qnty))}, '
          f'стоимость {sum(total_price):,} {word_money(sum(total_price))}.'.replace(',', ' '))
