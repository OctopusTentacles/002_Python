# ПОДКЛЮЧАЕМЫЕ МОДУЛИ

# КЛАССЫ 
# отделение классов из основного скрипта и их подключение

class Potato:
    states = {0: 'Отсутствует', 1: 'Росток', 2: 'Зеленая', 3: 'Зрелая'}

    def __init__(self, index):
        self.index = index
        self.state = 0

    def grow(self):
        if self.state < 3:
            self.state += 1
        self.print_state()

    def is_ripe(self):
        if self.state == 3:
            return True
        return False

    def print_state(self):
        print('Картошка {} сечас {}'.format(
            self.index, Potato.states[self.state]))


class PotatoGarden:
    def __init__(self, count):
        self.potatos = [Potato(index) for index in range(1, count + 1)]

    def grow_all(self):
        print('Картошка прорастает!')
        for potato in self.potatos:
            potato.grow()

    def are_all_ripe(self):
        if not all([i_potato.is_ripe() for i_potato in self.potatos]):
            print('Картошка еще не созрела!\n')
            return False
        else: 
            print('Вся картошка созрела. Можно собирать!\n')
            return True
        
    def print_all_states(self):
        for potato in self.potatos:
            potato.print_state()
