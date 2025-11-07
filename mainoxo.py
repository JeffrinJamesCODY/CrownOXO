import time
import random
import tkinter as tk # Tkinter library for GUI
import sys
from tkinter import font # Import font module from tkinter
import signal
#signal handling for ctrl-c in terminal to avoid traceback errors
def ctrl_c_handler():
    signal.signal(signal.SIGINT, signal.SIG_DFL)

    while True:
        print("Caught you!")
#oxo terminal game logic here which is imported from other files in the edited versions, this winning combo introduced the probability of ways players can win the game
def oxo_terminal_game(player1, player2):
    winningcombos = (
        (1, 2, 3), (4, 5, 6), (7, 8, 9),
        (1, 4, 7), (2, 5, 8), (3, 6, 9),
        (1, 5, 9), (3, 5, 7),
    )
    goes = 9
#function to display the game board in terminal, the grid is divided into 3 rows and 3 columns which is represented using list slicing.
    def play():
        print("\n", " | ".join(grid[:3]))
        print("---+---+---")
        print("", " | ".join(grid[3:6]))
        print("---+---+---")
        print("", " | ".join(grid[6:]))
#This function checks if a player has won by iterating through all winning combinations and checking if the player's symbol occupies all positions in any combination.
    def check_win(player):
        for combo in winningcombos:
            if all(grid[i - 1] == player for i in combo):
                return True
        return False
# Initializing the game grid with numbers 1-9 representing available positions. The game starts with player which is chosen first through coin flip.
    grid = list("123456789")
    player = player1
# The game runs for a maximum of 9 moves, alternating between players after each valid move.
    while goes > 1:
        play()
        try: # Prompting the current player to enter a position for their move. Input is validated to ensure it's an available space.
            space = int(input(f"Please enter a place for {player}: "))
            if str(space) not in grid: # Check if the space is already taken
                raise ValueError # Raise error if invalid, valueError is used here to handle invalid inputs
            grid[space - 1] = player
        except ValueError:
            print("Please enter the number of an open space (1–9).")
            continue
# After a valid move, check if the current player has won. If so, display the board and announce the winner.
        if check_win(player):
            play()
            print(f"Player {player} won!")
            break
# Switch players for the next turn.
        player = player1 if player == player2 else player2
        goes -= 1
# If all moves are exhausted without a winner, declare the game a draw.
    else:
        play()
        print("Draw!")


#OXO COIN FLIP UI FOR OXO
class OXOcoinflipUI(tk.Frame):
    def __init__(self, master, start_game_callback): # Initialize the coin flip UI frame
        super().__init__(master) # Call the parent class's constructor
        self.master = master # Reference to the main application window through master
        self.controller = master # Reference to the main application window through controller
        self.start_game_callback = start_game_callback # Callback function to start the OXO game
        self.choice = None # Variable to store player's choice (Heads or Tails)
        self.result_label = None
# Creates the UI widgets
        self.create_widgets()
# Function to create and layout the widgets in the coin flip UI
    def create_widgets(self):
        title = tk.Label(self, text="Player! This is your Coin Flip", font=("Impact", 24)) # Title label
        title.pack(pady=24)# Padding for spacing
# Instruction label for player one to choose heads or tails
        tk.Label(self, text="Player One, choose Heads or Tails:", font=("Impact", 16)).pack(pady=12)
# Frame to hold the choice buttons
        choice_frame = tk.Frame(self)
        choice_frame.pack()
# Buttons for choosing Heads or Tails
        tk.Button(choice_frame, text="Heads", font=("Impact"), width = 10, borderwidth= 5, command=lambda: self.set_choice("Heads")).pack(side="left", padx=10)
        tk.Button(choice_frame, text="Tails", font=("Impact"), width = 10, borderwidth = 5, command=lambda: self.set_choice("Tails")).pack(side = "right",padx=10)
        # Label to display results and messages
        self.result_label = tk.Label(self, text="", font=("Ariel", 14))
        self.result_label.pack(pady=22) # Padding for spacing
# Button to flip the coin
        self.flip_button = tk.Button(self, text="Flip Coin", font=("Impact", 13), width = 16, borderwidth = 7, command=self.flip_coin)
        self.flip_button.pack(pady=11)
# Function to set the player's choice of Heads or Tails for the coin flip
    def set_choice(self, choice):
        self.choice = choice
        self.result_label.config(text=f"You selected {choice} // Now you can flip the coin player!")
# Function to perform the coin flip and determine the outcome
    def flip_coin(self):
        if not self.choice: # Check if a choice has been made
            self.result_label.config(text="Choose Heads or Tails first to continue!") # Prompt the user to make a choice
            return # Exit the function if no choice is made
        # Simulate coin flip with a delay for effect
        self.result_label.config(text="Wait there! Hendon Heroes are flipping the coin...")
        self.master.update() # Update the UI to show the message
        time.sleep(1) 
# Randomly determine the outcome of the coin flip
        outcome = random.choice(["Heads", "Tails"])
        self.result_label.config(text=f"Hendon Heroes flipped the coin! The outcome is ... {outcome}!")
# Determine if Player One wins the coin flip
        if outcome == self.choice:
            winner_text = "Congratulations! Player One goes first!" # Message for Player One winning
        else:
            winner_text = "Tough Luck! Player Two goes first!" # Message for Player Two winning
# Display the result of the coin flip and provide option to start the OXO game
        tk.Label(self, text=winner_text, font=("Ariel", 16, "bold")).pack(pady=12)
        tk.Button(self, text="Start the OXO Game", font=("Impact", 13), width=16, borderwidth=7, command=lambda: start_oxo_game(self.controller)).pack(pady=11)

        self.controller.coin_flip_result = outcome # Store the outcome in the controller
        self.controller.winner_text = winner_text # Store the winner text in the controller

# Function to start the OXO game after the coin flip
def start_oxo_game(controller):
    print("Now loading OXO Game Board...")
    controller.destroy() # Close the coin flip UI using destroy method
    print("Launching OXO Game Board UI...")
    signal.signal(signal.SIGINT, signal.default_int_handler) # Restore default signal handler for Ctrl-C
    oxo_terminal_game("X", "O") # Start the OXO game in terminal mode with players X and O
    # Main application entry point
if __name__ == "__main__":
    root = tk.Tk() # Create the main application window using Tkinter and assign it to root
    root.iconbitmap(r'C:\Users\altar\Downloads\angelina-kelley-jinx.ico')
    root.title("CrownOXO Coin Flip by Team Hendon Heroes") # Set the window title
    root.geometry("600x400")# Set the window size
    coin_flip = OXOcoinflipUI(root, start_oxo_game) # Create the coin flip UI frame
    coin_flip.pack(fill="both", expand=True) # Pack the coin flip UI frame to fill the window
    root.mainloop() # Start the Tkinter event loop to run the application
