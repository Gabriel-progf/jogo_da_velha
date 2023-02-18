from Player import *


class Game_Board:

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
        
        if self.valid_position(line, column):

            if p == self.p1:
                self._board[line][column] = self.p1.symbol
            else:
                self._board[line][column] = self.p2.symbol
                
        

    def valid_position(self, line, column) -> bool:

        if self._board[line][column] != 0:
            raise Exception("Input symbol only in white zone in the board.")
        else:
            return True
    
    def player_win(self, p: Player):
        
        board = self._board      

        # 0,0
        if board[0][0] == p.symbol:
            if board[2][0] == p.symbol and board[4][0] == p.symbol or board[0][2] == p.symbol and board[0][4] == p.symbol or board[2][2] == p.symbol and board[4][4] == p.symbol:
                return p.symbol
            
        # 0,2
        elif board[0][2] == p.symbol:
            if board[0][0] == p.symbol and board[0][4] == p.symbol or board[2][2] == p.symbol and board[4][2] == p.symbol:
                return p.symbol
          
        # 0,4  
        elif board[0][4] == p.symbol:
            if board[0][0] == p.symbol and board[0][2] == p.symbol or board[2][4] == p.symbol and board[4][4] == p.symbol or board[2][2] == p.symbol and board[4][0] == p.symbol:
                return p.symbol
        # 2,0    
        elif board[2][0] == p.symbol:
            if board[0][0] == p.symbol and board[4][0] == p.symbol or board[2][2] == p.symbol and board[2][4] == p.symbol:
                return p.symbol
        
        # 4,0   
        elif board[4][0] == p.symbol:
            if board[0][0] == p.symbol and board[2][0] == p.symbol or board[4][2] == p.symbol and board[4][4] == p.symbol or board[2][2] == p.symbol and board[0][4] == p.symbol:
                return p.symbol
        
        # 2,2 
        elif board[2][2] == p.symbol:
            if board[0][0] == p.symbol and board[4][4] == p.symbol or board[0][2] == p.symbol and board[4][2] == p.symbol or board[2][0] == p.symbol and board[2][4] == p.symbol or board[0][4] == p.symbol and board[4][0] == p.symbol:
                return p.symbol
        
        # 4,2    
        elif board[4][2] == p.symbol:
            if board[4][0] == p.symbol and board[4][4] == p.symbol or board[2][2] == p.symbol and board[0][2] == p.symbol:
                return p.symbol
        
        # 4,4    
        elif board[4][4] == p.symbol:
            if board[4][0] == p.symbol and board[4][2] == p.symbol or board[2][4] == p.symbol and board[0][4] == p.symbol or board[2][2] == p.symbol and board[0][0] == p.symbol:
                return p.symbol
        
        # 2,4 
        elif board[2][4] == p.symbol:
            if board[0][4] == p.symbol and board[4][4] == p.symbol or board[2][2] == p.symbol and board[2][0] == p.symbol:
                return p.symbol

                
