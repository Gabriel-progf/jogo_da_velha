class Player:

    def __init__(self, name, symbol) -> None:
        self.name = name
        self.symbol = symbol

    def choose_position_symbol(self) -> tuple:

        line = int(input("Type position line: "))
        column = int(input("Type position column: "))
        
        range_num = range(1,4)
        
        if line not in range_num or column not in range_num:
            raise Exception("This zone is not valid. Type only number into 1 and 3.")

        line = 0 if line == 1 else line
        line = 4 if line == 3 else line

        column = 0 if column == 1 else column
        column = 4 if column == 3 else column

        return line, column
    
    def create_players():
        
        num_player = 1
        
        flagg = True
        while flagg:

                name = str(input(f"Name from Player {num_player}: "))

                if num_player == 1:
                    symbol = str(
                        input(f"Symbol from Player {num_player} [X,O]: ")).upper()

                if name.isdigit():
                    print("Type a name without number. Try again.")
                    continue

                if symbol not in 'XO':
                    print("The symbols must be only: X or O. Try again")
                    continue
                
                
                if symbol == 'X':
                    if num_player == 1:
                        player1 = Player(name, symbol)
                    else:
                        player2 = Player(name, "O")
                        flagg = None
                else:
                    if num_player == 1:
                        player1 = Player(name, symbol)
                    else:
                        player2 = Player(name, "X")
                        flagg = None


                num_player = 1 if num_player == 2 else 2
                
        return player1, player2
                

           
            

