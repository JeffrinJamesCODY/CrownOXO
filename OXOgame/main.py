import time
import random
import webbrowser
import tkinter as tk
from tkinter import font
from oxoterminalboard import oxo_terminal_game
import subprocess
import sys

# UI for coin flip of OXO game
class OXOcoinflipUI(tk.Frame):
    def __init__(self, master, start_game_callback):
        super().__init__(master)
        self.master = master
        self.controller = master
        self.start_game_callback = start_game_callback
        self.choice = None
        self.result_label = None

        self.create_widgets()

    def create_widgets(self):
        title = tk.Label(self, text="Player! This is your Coin Flip", font=("Impact", 24))
        title.pack(pady=24)

        tk.Label(self, text="Player One, choose Heads or Tails:", font=("Impact", 16)).pack(pady=12)

        choice_frame = tk.Frame(self)
        choice_frame.pack()

        tk.Button(choice_frame, text="Heads", font=("Impact"), width = 10, borderwidth= 5, command=lambda: self.set_choice("Heads")).pack(side="left", padx=10)
        tk.Button(choice_frame, text="Tails", font=("Impact"), width = 10, borderwidth = 5, command=lambda: self.set_choice("Tails")).pack(side = "right",padx=10)
        
        self.result_label = tk.Label(self, text="", font=("Ariel", 14))
        self.result_label.pack(pady=22)

        self.flip_button = tk.Button(self, text="Flip Coin", font=("Impact", 13), width = 16, borderwidth = 7, command=self.flip_coin)
        self.flip_button.pack(pady=11)

    def set_choice(self, choice):
        self.choice = choice
        self.result_label.config(text=f"You selected {choice} // Now you can flip the coin player!")

    def flip_coin(self):
        if not self.choice:
            self.result_label.config(text="Choose Heads or Tails first to continue!")
            return
        
        self.result_label.config(text="Wait there! Hendon Heroes are flipping the coin...")
        self.master.update()
        time.sleep(1)

        outcome = random.choice(["Heads", "Tails"])
        self.result_label.config(text=f"Hendon Heroes flipped the coin! The outcome is ... {outcome}!")

        if outcome == self.choice:
            winner_text = "Congratulations! Player One goes first!"
        else:
            winner_text = "Tough Luck! Player Two goes first!"

        tk.Label(self, text=winner_text, font=("Ariel", 16, "bold")).pack(pady=12)
        tk.Button(self, text="Start the OXO Game", font=("Impact", 13), width=16, borderwidth=7, command=lambda: start_oxo_game(self.controller)).pack(pady=11)

        self.controller.coin_flip_result = outcome
        self.controller.winner_text = winner_text


def start_oxo_game(controller):
    print("Now loading OXO Game Board...")
    controller.destroy()
    print("Launching OXO Game Board UI...")
    oxo_terminal_game("X", "O")
    subprocess.run([sys.excutable, "oxoterminalboard.py"])
    
if __name__ == "__main__":
    root = tk.Tk()
    root.iconbitmap(r'C:\Users\altar\Downloads\angelina-kelley-jinx.ico')    
    root.title("CrownOXO Coin Flip by Team Hendon Heroes")
    root.geometry("600x400")
    coin_flip = OXOcoinflipUI(root, start_oxo_game)
    coin_flip.pack(fill="both", expand=True)
    root.mainloop()

























# UI for OXO Game Board
# class OXOGameBoard(tk.Frame):
#     def __init__(self, master, controller):
#         super().__init__(master)
#         self.master = master
#         self.controller = controller
#         self.title("OXO Game")
#         self._cells = {}
#         self._oxo_boarddisplay()
#         self._oxo_boardgrid()

#         def oxo_boarddisplay(self):
#             display_frame = tk.Frame(master=self)
#             display_frame.pack(fill=tk.X)
#             self.display = tk.Label(
#                 master=display_frame,
#                 text="Welcome to OXO! Ready to play? Click a cell to start.",
#                 font=font.Font(size=20, weight="bold"),
#             )
#             self.display.pack()

#         def oxo_boardgrid(self):
#             grid_frame = tk.Frame(master=self)
#             grid_frame.pack()
#             for row in range(3):
#                 self.rowconfigure(row, weight=1, minsize=75)
#                 self.columnconfigure(row, weight=1, minsize=100)
#                 for col in range(3):
#                     button = tk.Button(
#                         master=grid_frame,
#                         text="",
#                         font=("Ariel", 32, "bold"),
#                         width=4,
#                         height=3,
#                         highlightbackground="Fuchsia",
#                     )
#                     self._cells[button] = (row,col)
#                     button.grid(
#                         row=row,
#                         column=col,
#                         padx=5,
#                         pady=5,
#                         sticky="nsew",
#                     )

# def main():
#     board = OXOGameBoard()
#     board.mainloop()

# if __name__ == "__main__":
#     main()



        
