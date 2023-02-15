from Board import *

if __name__ == '__main__':
    
    try:
        board = Board()
        
        board.print_board()

        position_line = int(input("Type position line: "))
        position_column = int(input("Type position column: "))

        position_line = 0 if position_line == 1 else position_line
        position_line = 4 if position_line == 3 else position_line

        position_column = 0 if position_column == 1 else position_column
        position_column = 4 if position_column == 3 else position_column
        
        
        print(position_line, position_column)



    except:
        ...