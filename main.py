from GameBoard import *
from Player import *
import os

if __name__ == '__main__':

    id_player = 1

   
    count = 0
    verific_creation_of_players = True
    
    winner = None

    while True:

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
                
                winner = board.player_win(player1)
                
                id_player = 2
            else:
                print(f"==== Player {id_player}: {player2.name} ====")
                line, column = board.p2.choose_position_symbol()

                board.input_symbol(line, column, player2)
                
                winner = board.player_win(player2)

                id_player = 1
            
                
            os.system('clear')
            
            count += 1
            
            if winner:
                board.print_board()
                print("==========================")
                print(f"PLAYER: {winner.name}")
                print(f"{winner.symbol} WIN!")
                print("==========================")
                break
            elif board.game_tie(winner, count):
                
                board.print_board()
                print("==========================")
                print(f"        GAME TIA         ") 
                print("==========================")
                break
            
        except Exception as e:
            print(e)
