class Player:

    def __init__(self, name, symbol) -> None:
        self.name = name
        self.symbol = symbol

    def choose_position_symbol(self) -> tuple:

        line = int(input("Type position line: "))
        column = int(input("Type position column: "))
        
        range_num = range(1,4)
        
        if line not in range_num or column not in range_num:
            raise Exception("This line is not valid. Type only number into 1 and 3.")

        line = 0 if line == 1 else line
        line = 4 if line == 3 else line

        column = 0 if column == 1 else column
        column = 4 if column == 3 else column

        return line, column
