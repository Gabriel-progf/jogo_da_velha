"""
     0 1 2 3 4
          
0    0 1 0 1 0
1    1 1 1 1 1
2    0 1 0 1 0
3    1 1 1 1 1
4    0 1 0 1 0

"""


from Board import *
from Player import *

if __name__ == '__main__':

    num_player = 1

    flag = True

    flagg = True

    while flag:

        try:

            while flagg:

                name = str(input(f"Name from Player {num_player}: "))

                symbol = str(
                    input(f"Symbol from Player {num_player}: ")).upper()

                if name.isdigit():
                    print("Type a name without number. Try again.")
                    continue

                if symbol not in 'XO':
                    print("The symbols must be only: X or O. Try again")
                    continue

                if num_player == 1:
                    player1 = Player(name, symbol)
                else:
                    player2 = Player(name, symbol)
                    flagg = None

                num_player = 1 if num_player == 2 else 2

            board = Board(player1, player2)

            board.print_board()

            if num_player == 1:
                print(f"==== Player {num_player}: {player1.name} ====")
                line, column = board.p1.choose_position_symbol()

                board.input_symbol(line, column, player1)
                num_player = 2
            else:
                print(f"==== Player {num_player}: {player2.name} ====")
                line, column = board.p2.choose_position_symbol()
                board.input_symbol(line, column, player2)
                num_player = 1

        except ValueError as e:
            print(e)
