from Player import *


class Board:

    def __init__(self,  p1: Player, p2: Player) -> None:
        self.p1 = p1
        self.p2 = p2

    _board = [
        [0, '|', 0, '|', 0],
        ['_', '|', '_', '|', '_'],
        [0, '|', 0, '|', 0],
        ['_', '|', '_', '|', '_'],
        [0, '|', 0, '|', 0]
    ]

    def print_board(self) -> None:
        print('\n')

        print('   ', end='')
        for i, item in enumerate(self._board):
            if i % 2 != 0:
                print('   ', end='')
            else:
                i += 1 if i == 0 else 0
                x = i - 1 if i == 4 else i
                print(f'{x}   ', end='')

        for i, item in enumerate(self._board):
            print('\n')
            if i % 2 != 0:
                print('   ', end='')
            else:
                i += 1 if i == 0 else 0
                x = i - 1 if i == 4 else i
                print(f'{x}  ', end='')
            for j in item:
                if j == 0:
                    j = " "

                print(f' {j}  ', end='')
        print('\n')
        print('\n')

    def input_symbol(self, line, column, p: Player) -> None:

        if p == self.p1:
            self._board[line][column] = self.p1.symbol
        else:
            self._board[line][column] = self.p2.symbol

    def valid_position() -> bool:
        ...
