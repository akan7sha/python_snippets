import tkinter as tk
from tkinter import messagebox
import random


class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("AI Tic Tac Toe")
        self.current_player = 'X'  # Human player
        self.ai_player = 'O'  # AI player
        self.board = ['' for _ in range(9)]
        self.buttons = []

        # Create game board
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(self.window, text='', width=20, height=10,
                                   command=lambda row=i, col=j: self.make_move(row, col))
                button.grid(row=i, column=j)
                row.append(button)
            self.buttons.append(row)

    def make_move(self, row, col):
        index = 3 * row + col

        # Check if the cell is empty
        if self.board[index] == '':
            # Human move
            self.board[index] = self.current_player
            self.buttons[row][col].config(text=self.current_player)

            # Check if game is over after human move
            if self.check_winner(self.current_player):
                messagebox.showinfo("Game Over", "You win!")
                self.reset_game()
                return
            elif self.is_board_full():
                messagebox.showinfo("Game Over", "It's a draw!")
                self.reset_game()
                return

            # AI move
            self.ai_move()

            # Check if game is over after AI move
            if self.check_winner(self.ai_player):
                messagebox.showinfo("Game Over", "AI wins!")
                self.reset_game()
            elif self.is_board_full():
                messagebox.showinfo("Game Over", "It's a draw!")
                self.reset_game()

    def ai_move(self):
        """Make the best possible move using minimax algorithm"""
        best_score = float('-inf')
        best_move = None

        # Try all possible moves and choose the best one
        for i in range(len(self.board)):
            if self.board[i] == '':
                self.board[i] = self.ai_player
                score = self.minimax(self.board, 0, False)
                self.board[i] = ''

                if score > best_score:
                    best_score = score
                    best_move = i

        # Make the best move
        if best_move is not None:
            self.board[best_move] = self.ai_player
            row = best_move // 3
            col = best_move % 3
            self.buttons[row][col].config(text=self.ai_player)

    def minimax(self, board, depth, is_maximizing):
        """Minimax algorithm for finding the best move"""
        # Check terminal states
        if self.check_winner(self.ai_player):
            return 1
        if self.check_winner(self.current_player):
            return -1
        if self.is_board_full():
            return 0

        if is_maximizing:
            best_score = float('-inf')
            for i in range(len(board)):
                if board[i] == '':
                    board[i] = self.ai_player
                    score = self.minimax(board, depth + 1, False)
                    board[i] = ''
                    best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for i in range(len(board)):
                if board[i] == '':
                    board[i] = self.current_player
                    score = self.minimax(board, depth + 1, True)
                    board[i] = ''
                    best_score = min(score, best_score)
            return best_score

    def check_winner(self, player):
        """Check if the given player has won"""
        # Check rows
        for i in range(0, 9, 3):
            if self.board[i] == self.board[i + 1] == self.board[i + 2] == player:
                return True

        # Check columns
        for i in range(3):
            if self.board[i] == self.board[i + 3] == self.board[i + 6] == player:
                return True

        # Check diagonals
        if self.board[0] == self.board[4] == self.board[8] == player:
            return True
        if self.board[2] == self.board[4] == self.board[6] == player:
            return True

        return False

    def is_board_full(self):
        """Check if the board is full"""
        return '' not in self.board

    def reset_game(self):
        """Reset the game to initial state"""
        self.board = ['' for _ in range(9)]
        for row in self.buttons:
            for button in row:
                button.config(text='')

    def run(self):
        """Start the game"""
        self.window.mainloop()


if __name__ == "__main__":
    game = TicTacToe()
    game.run()