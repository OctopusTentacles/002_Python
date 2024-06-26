# Задача 2. Семья
# Реализуйте класс «Семья», который состоит из атрибутов «Имя», Деньги» и 
# «Наличие дома» и объекты которого могут выполнять следующие действия:

# Отобразить информацию о себе.
# Заработать денег (подаётся число, которое прибавляется к текущему значению денег).
# Купить дом (подаётся стоимость дома и необязательный аргумент «Скидка»). 
# Вывести соответствующее сообщение об успешной/неуспешной покупке дома.
# Создайте как минимум один экземпляр класса и проверьте работу методов.

# Пример работы программы (вывод информации, покупка дома, заработок, очередная покупка):
# Family name: Common family
# Family funds: 100000
# Having a house: False

# Try to buy a house
# Not enough money!

# Earned 800000 money! Current value: 900000
# Try to buy a house again
# House purchased! Current money: 0.0

# Family name: Common family
# Family funds: 0.0
# Having a house: True


class Family:
    name = ''
    money = 0
    house = False

    def print_info(self):
        print('\nFamily name: {}\nFamily funds: {}\nHaving a house: {}'.format(
                self.name, self.money, self.house))
        
    def get_money(self, count):
        self.money += count
        print(f'\nEarned {count} money! Current value: {self.money}')

    def buy_a_house(self, price, discount=0):
        house_price = (price - price * (discount / 100))
        print('\nTry to buy a house')
        if self.money >= house_price:
            self.money -= house_price
            print(f'House purchased! Current money: {self.money}')
            self.house = True
        else:
            print('Not enough money!')

human = Family()
human.name = 'Common family'
human.money = 100000

human.print_info()
house_price = 900000
human.buy_a_house(house_price)
human.get_money(house_price - human.money)
human.buy_a_house(house_price)
human.print_info()