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
        
        linee = line
        columnn = column

        if self.valid_position(linee, columnn):

            if p == self.p1:
                self._board[line][column] = self.p1.symbol
            else:
                self._board[line][column] = self.p2.symbol
                
        

    def valid_position(self, line, column) -> bool:

        if self._board[line][column] != 0:
            raise Exception("Input symbol only in white zone in the board.")
        else:
            return True
    
    def player_win(self, board):
                
        op1 = [(0,0),(0,2),(0,4)] 
        op2 = [(2,0),(2,2),(2,4)] 
        op3 = [(4,0),(4,2),(4,4)]


        op4 = [(0,0),(2,0),(4,0)] 
        op5 = [(0,2),(2,2),(4,2)]
        op6 = [(0,4),(2,4),(4,4)]  

        op7 = [(0,0),(2,2),(4,4)] 
        op8 = [(0,4),(2,2),(4,0)]
            
        opctions_to_win = [op1,op2,op3,op4,op5,op6,op7,op8]


        positions_array_O = []
        positions_array_X = []
        
        for i in range(0,5):
            for j in range(0,5):
                if board[i][j] == 'O':
                    positions_array_O.append((i,j))
                elif board[i][j] == 'X':
                    positions_array_X.append((i,j))

        filter_positions_O = []

        for ops in opctions_to_win:
            for op in ops:
                if op in positions_array_O:
                    if op not in filter_positions_O:
                        filter_positions_O.append(op)
                

        filter_opctions_to_win_O = filter_positions_O[:3].copy()

        for ops in opctions_to_win:          
            if filter_opctions_to_win_O == ops:
                return 'O' 

        filter_positions_X = []

        for ops in opctions_to_win:
            for op in ops:
                if op in positions_array_X:
                    if op not in filter_positions_X:
                        filter_positions_X.append(op)
                

        filter_opctions_to_win_X = filter_positions_X[:3].copy()

        for ops in opctions_to_win:
            if filter_opctions_to_win_X == ops:
                return 'X'
    
        print(f"{filter_opctions_to_win_O=},{filter_opctions_to_win_X=}")


        

                
