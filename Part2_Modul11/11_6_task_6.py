# Задача 06. Крестики-нолики
# Что нужно сделать
# Напишите программу, которая реализует игру «Крестики-нолики». 
# Да, это всё условие задачи.

# Ваши классы в этой задаче могут выглядеть так:


import time


class Cell:
    def __init__(self, num):
        self.sym_cell = ' '
        self.num = num
        
    def __str__(self):
        return str(self.num)


# ---------------------------------------------------------------------------------------
class Board:
    '''поле игры'''
    # Класс поля, который создаёт у себя экземпляры клетки
    def __init__(self):
    # доска 3х3, делаем список из экземпляров Сell() с номером от 1 до 9 
        self.num_cell = [Cell(cell) for cell in range(1, 10)]

    def show_board(self):
        for raw in range(3):
            print('       |       |')
            for cul in range(3):
                print('   \033[2;30m{}\033[0m'.format
                      (self.num_cell[raw * 3 + cul]), end='')
                if cul < 2:
                    print('   |',end='')
            print('\n       |       |')
            if raw < 2:
                print('-' * 23)

# ---------------------------------------------------------------------------------------
class Player:
#  У игрока может быть
#   - имя
#   - на какую клетку ходит
    def __init__(self, name, marker, score = 0):
        self.name = name
        self.marker = marker
        self.score = score
        self.board = Board()

    def __str__(self):
        return (f'{self.name} - {self.marker}, score: {str(self.score)}')

    # def win_point(self, marker):
    #     self.marker = marker
    #     self.score += 1


    def choose_cell(self, player):
        while True:
            try:
                print('\nTurn', player.marker, end=', ')
                num_cell = int(input('choose cell number: '))
               
                if num_cell not in (1,2,3,4,5,6,7,8,9):
                    raise ValueError
                if self.board.num_cell[num_cell - 1] in (
                    '\033[1;32mX\033[0m', '\033[1;33mO\033[0m'):
                    raise Exception
                
                self.board.num_cell[num_cell - 1] = player.marker
                return player.marker
            
            except ValueError:
                print('\033[1;31mEnter number from 1 to 9!\033[0m')
                continue
            except Exception:
                print('\033[1;31mCell is occupied, select another!\033[0m')
                continue
        

    def choose_marker():
        marker_1 = '\033[1;32mX\033[0m'
        marker_2 = '\033[1;33mO\033[0m'

        name_1 = input(f'choose {marker_1} or {marker_2}: ')
        name_2 = ''
        if name_1 == 'x':
            name_1 = Player('Player_1', marker_1)
            name_2 = Player('Player_2', marker_2)
        else:
            name_1 = Player('Player_1', marker_2)
            name_2 = Player('Player_2', marker_1)
        return name_1, name_2
        
# ---------------------------------------------------------------------------------------
class Game:    
    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2
        self.score = 0
        self.round = 1
        self.step = 0
        self.board = Board()
        # класс «Игры» содержит атрибуты:
        # состояние игры,
        # игроки,
        # поле.
        # А также методы:

    def __str__(self):
        return self.player_1, self.player_2

    def display(self):
        print(f'{self.player_1} |'
              f'\n{self.player_2} |')

    def delay(self):
        for _ in range(27):
            print('.', end='', flush=True)
            time.sleep(0.04)
    
    def new_step(self):
        # Метод запуска одного хода игры. Получает одного из игроков, 
        # запрашивает у игрока номер клетки, изменяет поле, проверяет, 
        # выиграл ли игрок. Если игрок победил, возвращает True, иначе False.
        if self.step % 2 == 0:
            num_cell = Player.choose_cell(self, self.player_2)
        else:
            num_cell = Player.choose_cell(self, self.player_1)
        
        check_win = ((0, 1, 2), (3, 4, 5), (6, 7, 8),
                     (0, 3, 6), (1, 4, 7), (2, 5, 8),
                     (0, 4, 8), (2, 4, 6))
        for cell in check_win:
            for symbol in cell:
                if self.board.num_cell[symbol] != num_cell:
                    break
            else:
                
                return True


    def new_round(self):
        # Метод запуска одной игры. Очищает поле, запускает цикл с игрой, 
        # который завершается победой одного из игроков или ничьей. 
        # Если игра завершена, метод возвращает True, иначе False.
        self.step = 1
        self.delay()
        print('\nRound', self.round)
        self.display()
        self.board = Board()
        
        while True:
            self.board.show_board()
            if self.new_step():
                self.score += 1
                
                self.board.show_board()
                print('=====WIN=====')
                self.display()
                
                return True

            else:
                self.step += 1
                if self.step == 9:
                    self.board.show_board()
                    print('THIS ROUND IS A DRAW!')
                    break
        

    def new_game(self):
        # Основной метод запуска игр. В цикле запускает игры, запрашивая 
        # после каждой игры, хотят ли игроки продолжать играть. 
        # После каждой игры выводится текущий счёт игроков.
        self.delay()

        print('\nNew Game')
        

        while self.round < 4:
            out = input('press ENTER for continue\npress 0 for Exit  ')
            if out == '0':
                break
            if self.new_round():
                continue

            self.round += 1


    def greating():
        print('\n      TIC TAC TOE')
        input('press ENTER for new game...')

       

# MAIN CODE====================================================================
start = Game.greating()
player_1, player_2 = Player.choose_marker()

game = Game(player_1, player_2)
game.new_game()