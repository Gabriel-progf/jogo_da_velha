"""
     0 1 2 3 4
          
0    0 1 0 1 0
1    1 1 1 1 1
2    0 1 0 1 0
3    1 1 1 1 1
4    0 1 0 1 0

"""


from GameBoard import *
from Player import *
import os

if __name__ == '__main__':

    id_player = 1

    flag = True

    verific_creation_of_players = True
    
    qtd_symbol = 0

    while flag:

        try:

            if verific_creation_of_players:
                player1, player2 = Player.create_players()
                verific_creation_of_players = False

            board = Game_Board(player1, player2)
            board.print_board()

            if id_player == 1:
                print(f"==== Player {id_player}: {player1.name} ====")
                line, column = board.p1.choose_position_symbol()

                board.input_symbol(line, column, player1)
                qtd_symbol += 1

                id_player = 2
            else:
                print(f"==== Player {id_player}: {player2.name} ====")
                line, column = board.p2.choose_position_symbol()

                board.input_symbol(line, column, player2)
                qtd_symbol += 1

                id_player = 1


            result_game = board.player_win(Game_Board._board)
            
            print(result_game)
            
            if result_game != None:
                print("=====================")
                if result_game == player1.symbol:
                        print(f"The Player {player1.symbol} is the winner!! ")
                        print(f"Congratulations {player1.name}")
                        
                
                elif result_game == player2.symbol:
                        print(f"The Player {player2.symbol} is the winner!! ")
                        print(f"Congratulations {player2.name}")
                
                print("=====================")
            
                break
            
            # if qtd_symbol == 9 and result_game == None:
            #     print("No player win!!!!")
        
                

            # os.system('clear')

        except ValueError as e:
            print(e)

        except Exception as e:
            print(e)
