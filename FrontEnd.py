from main import Tictactoe


import tkinter as tk
from tkinter import messagebox

class TicTacToeGUI:

    def __init__(self, root, game):
        self.root = root
        self.game = game
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_board()
        self.update_title()

    def create_board(self):
        for row in range(3):
            for col in range(3):
                btn = tk.Button(self.root, text="", font=('Helvetica', 24), width=5, height=2,
                                command=lambda r=row, c=col: self.on_click(r, c))
                btn.grid(row=row, column=col)
                self.buttons[row][col] = btn

    def on_click(self, row, col):
        if self.game.board[row][col] != ',':
            return

        self.game.player_move(row, col)
        self.update_board()

        win, player, symbol = self.game.check_winner(self.game.board)
        if win:
            messagebox.showinfo("Game Over", f"{player} ({symbol}) wins!")
            self.game.new_game()
            self.update_board()
        elif not self.game.check_if_moves():
            messagebox.showinfo("Game Over", "It's a tie!")
            self.game.new_game()
            self.update_board()
        else:
            self.update_title()

    def update_board(self):
        for row in range(3):
            for col in range(3):
                value = self.game.board[row][col]
                self.buttons[row][col]['text'] = '' if value == ',' else value

    def update_title(self):
        turn = self.game.player_1[0] if self.game.player_turn % 2 == 0 else self.game.player_2[0]
        self.root.title(f"Tic-Tac-Toe - {turn}'s Turn")

# Run GUI
if __name__ == "__main__":
    from tkinter import Tk
    root = Tk()
    root.title("Tic-Tac-Toe")
    game = Tictactoe("Player 1", "Player 2")
    gui = TicTacToeGUI(root, game)
    root.mainloop()
