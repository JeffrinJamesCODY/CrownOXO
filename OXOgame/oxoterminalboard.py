import time
import random
goes = 9
def oxo_terminal_game(player1, player2):
    winningcombos = (
        (1, 2, 3), (4, 5, 6), (7, 8, 9),
        (1, 4, 7), (2, 5, 8), (3, 6, 9),
        (1, 5, 9), (3, 5, 7),
    )

    def play():
        print("\n", " | ".join(grid[:3]))
        print("---+---+---")
        print("", " | ".join(grid[3:6]))
        print("---+---+---")
        print("", " | ".join(grid[6:]))

    def check_win(player):
        for combo in winningcombos:
            if all(grid[i - 1] == player for i in combo):
                return True
        return False

    grid = list("123456789")
    player = player1

    while goes > 1:
        play()
        try:
            space = int(input(f"Please enter a place for {player}: "))
            if str(space) not in grid:
                raise ValueError
            grid[space - 1] = player
        except ValueError:
            print("Please enter the number of an open space (1–9).")
            continue

        if check_win(player):
            play()
            print(f"Player {player} won!")
            break

        player = player1 if player == player2 else player2
        goes -= 1

    else:
        play()
        print("Draw!")
