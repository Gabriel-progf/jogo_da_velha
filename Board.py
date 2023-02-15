class Board:

    board = [
        [0, ' | ', 0, ' | ', 0],
        ['-', ' | ', '-', ' | ', '-'],
        [0, ' | ', 0, ' | ', 0],
        ['-', ' | ', '-', ' | ', '-'],
        [0, ' | ', 0, ' | ', 0]
    ]

    def print_board(self) -> None:
        print('\n')
        
        print('   ', end='')
        for i, item in enumerate(self.board):
            if i % 2 != 0:
                print('   ', end='')
            else:
                i += 1 if i == 0 else 0
                x = i - 1 if i == 4 else i
                print(f'{x}  ', end='')


        for i, item in enumerate(self.board):
            print('\n')
            if i % 2 != 0:
                print('   ', end='')
            else:
                i += 1 if i == 0 else 0
                x = i - 1 if i == 4 else i
                print(f'{x}  ', end='')
            for j in item:
                print(f'{j} ', end='')
        print('\n')
        print('\n')
        
    
    def input_symbol(self, line, column):
        ...

        
    
    def valid_win():
        ...
    
