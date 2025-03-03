import tkinter as tk
from tkinter import messagebox
import time

# Global variables
root = tk.Tk()
root.title("Tic Tac Toe with Player")
board = [['', '', ''], ['', '', ''], ['', '', '']]
current_player = 'X'
moves = 0
timer_running = False
start_time = None

buttons = []
timer_label = None


def make_move(row, col):
    global current_player, moves, timer_running

    if board[row][col] == '':
        board[row][col] = current_player
        buttons[row][col]['text'] = current_player
        moves += 1

        if moves == 1 and not timer_running:
            start_timer()

        if check_winner(current_player):
            stop_timer()
            tk.messagebox.showinfo('Game Over', f'Player {current_player} wins!')
            reset_game()
        elif moves == 9:
            stop_timer()
            tk.messagebox.showinfo('Game Over', 'It\'s a draw!')
            reset_game()
        else:
            current_player = 'O' if current_player == 'X' else 'X'


def check_winner(player):
    # Check rows
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True

    # Check columns
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] == player:
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False


def start_timer():
    global timer_running, start_time
    timer_running = True
    start_time = time.time()
    update_timer()


def stop_timer():
    global timer_running
    timer_running = False


def update_timer():
    global timer_label, timer_running, start_time
    if timer_running:
        elapsed_time = time.time() - start_time
        minutes = int(elapsed_time // 60)
        seconds = int(elapsed_time % 60)
        time_str = f'{minutes:02d}:{seconds:02d}'
        timer_label['text'] = time_str
        timer_label.after(1000, update_timer)


def reset_game():
    global board, current_player, moves
    board = [['', '', ''], ['', '', ''], ['', '', '']]
    current_player = 'X'
    moves = 0

    for row in buttons:
        for button in row:
            button['text'] = ''

    timer_label['text'] = '00:00'


def main():
    global buttons, timer_label
    buttons = []

    for i in range(3):
        row = []
        for j in range(3):
            button = tk.Button(root, text='', width=10, height=5, command=lambda x=i, y=j: make_move(x, y))
            button.grid(row=i, column=j)
            row.append(button)
        buttons.append(row)

    timer_label = tk.Label(root, text='00:00')
    timer_label.grid(row=3, columnspan=3)

    root.mainloop()


if __name__ == '__main__':
    main()