import time
import random

def get_player_move(player):
    while True:
        move = int(input(f"Player{player},choose a position(1-9):"))
        if move <0 or move > 8:
            print("Choose a number between 1 and 9. ")
            elif board[move] !='':
                print("That spot is already taken. Choose another!")
                else:
                    return
                move except ValueError:
                    print("Invalid input! Please enter a number between 1 and 9.")
