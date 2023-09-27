# Задача 06. Крестики-нолики
# Что нужно сделать
# Напишите программу, которая реализует игру «Крестики-нолики». 
# Да, это всё условие задачи.

# Ваши классы в этой задаче могут выглядеть так:

class Cell:
# Клетка, у которой есть значения   
    def __init__(self, num):
# занята клетка или нет
        self.sym_cell = ' '
# номер клетки
        self.num = num
        
# __str__ – метод для отображения информации об объекте класса для пользователей 
# благодаря этому методу в строке 38 мы видим в поле игры цифры 
    def __str__(self):
        return str(self.num)



class Board:
    '''поле игры'''
    # Класс поля, который создаёт у себя экземпляры клетки
    def __init__(self):
    # доска 3х3, делаем список из экземпляров Сell() с номером от 1 до 9 
        self.num_board = [Cell(cell) for cell in range(1, 10)]

    def show_board(self):
        # делаем линии поля жирными
        for raw in range(3):
            print('\n' + '\033[1m-' * 19)
            print('|', end=' ')
            # в ячеку вписываем цифры, чтобы игрок как-то мог выбрать куда ходить
            # и делеам их менее заметными 
            for cul in range(3):
                print(f' \033[2m{self.num_board[raw * 3 + cul]}\033[0m  | ', end='')
        print('\n' + '\033[1m-\033[0m' * 19)


class Player:
#  У игрока может быть
#   - имя
#   - на какую клетку ходит
    def __init__(self, name, cell_num):
        self.name = name
        self.cell_num = cell_num
        self.score = 0

    def choose_cell(self):
        try:
            self.cell_num = int(input(self.name, 'choose cell number: '))
        except ValueError:
        
    def choose_marker():
        marker_1 = '\033[1;32mX\033[0m'
        marker_2 = '\033[1;33mO\033[0m'

        name_1 = input(f'choose {marker_1} or {marker_2}: ')
        name_2 = ''
        if name_1 == 'x':
            name_1 = marker_1
            name_2 = marker_2
        else:
            name_1 = marker_2
            name_2 = marker_1
        return name_1, name_2
        

    #     print('Игрок_1 = ')

    #     pass

class Game:    
    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2
        self.board = Board()
    # класс «Игры» содержит атрибуты:
    # состояние игры,
    # игроки,
    # поле.
    # А также методы:
    
    def new_step(self, index, marker):
        # Метод запуска одного хода игры. Получает одного из игроков, 
        # запрашивает у игрока номер клетки, изменяет поле, проверяет, 
        # выиграл ли игрок. Если игрок победил, возвращает True, иначе False.


        if (9 < index < 1 or Board.num_board[index - 1] in ('X', 'O')):
            return False
        Board.num_board[index - 1] = marker



        # while True:
        #     step = input('Куда ходим: ' + marker)
        #     if not (step in '123456789'):
        #         print('Повторите ввод.')
        #         continue

        pass

    def new_round(self):
        # Метод запуска одной игры. Очищает поле, запускает цикл с игрой, 
        # который завершается победой одного из игроков или ничьей. 
        # Если игра завершена, метод возвращает True, иначе False.
        round = 1
        print('Round', round)
        player_1, player_2 = Player.choose_marker()
        print(f'\nPlayer_1 - {player_1}, Player_2 - {player_2}')
        player_1 = Player(player_1, player_1)
        player_2 = Player(player_2, player_2)
        self.board = Board()
        self.board.show_board()
        

        

    def new_game(self):
        # Основной метод запуска игр. В цикле запускает игры, запрашивая 
        # после каждой игры, хотят ли игроки продолжать играть. 
        # После каждой игры выводится текущий счёт игроков.
        print('New Game')
        self.new_round()
       

# MAIN CODE===========================================================
print('\tTIC TAC TOE')
input('press ENTER for new game')
player_1, player_2 = Player.choose_marker()

# print(f'\nPlayer_1 - {player_1}, Player_2 - {player_2}')
# player_1 = Player(player_1, player_1)
# player_2 = Player(player_2, player_2)

game = Game(player_1, player_2)
game.new_game()