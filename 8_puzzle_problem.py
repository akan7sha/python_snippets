import tkinter as tk
from tkinter import messagebox
import random
import copy
import heapq
from collections import deque


class PuzzleState:
    def __init__(self, board, parent=None, move="", cost=0):
        self.board = board
        self.parent = parent
        self.move = move
        self.cost = cost
        self.blank_pos = self.find_blank()
        self.hash = str(self.board)

    def find_blank(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 0:
                    return (i, j)

    def get_neighbors(self):
        neighbors = []
        i, j = self.blank_pos
        moves = [
            ("Up", -1, 0),
            ("Down", 1, 0),
            ("Left", 0, -1),
            ("Right", 0, 1)
        ]

        for move, dx, dy in moves:
            ni, nj = i + dx, j + dy
            if 0 <= ni < 3 and 0 <= nj < 3:
                new_board = copy.deepcopy(self.board)
                new_board[i][j], new_board[ni][nj] = new_board[ni][nj], new_board[i][j]
                neighbors.append(PuzzleState(new_board, self, move, self.cost + 1))

        return neighbors

    def __lt__(self, other):
        return self.cost < other.cost

    def __eq__(self, other):
        return self.board == other.board

    def __hash__(self):
        return hash(self.hash)


class EightPuzzleGame:
    def __init__(self, master):
        self.master = master
        self.master.title("8-Puzzle Game")
        self.master.resizable(False, False)

        # Initialize the game state
        self.goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        self.current_state = None
        self.moves_count = 0
        self.solution_steps = []
        self.step_index = 0

        # Create frames
        self.main_frame = tk.Frame(master, padx=20, pady=20)
        self.main_frame.pack()

        self.grid_frame = tk.Frame(self.main_frame)
        self.grid_frame.pack(pady=10)

        self.button_frame = tk.Frame(self.main_frame)
        self.button_frame.pack(pady=10)

        # Create buttons for the grid
        self.grid_buttons = []
        for i in range(3):
            row_buttons = []
            for j in range(3):
                button = tk.Button(self.grid_frame, width=5, height=2, font=('Arial', 16, 'bold'),
                                   command=lambda i=i, j=j: self.move_tile(i, j))
                button.grid(row=i, column=j, padx=5, pady=5)
                row_buttons.append(button)
            self.grid_buttons.append(row_buttons)

        # Create control buttons
        self.new_game_button = tk.Button(self.button_frame, text="New Game",
                                         command=self.new_game, width=10)
        self.new_game_button.grid(row=0, column=0, padx=5)

        self.solve_button = tk.Button(self.button_frame, text="Solve",
                                      command=self.solve_puzzle, width=10)
        self.solve_button.grid(row=0, column=1, padx=5)

        self.next_step_button = tk.Button(self.button_frame, text="Next Step",
                                          command=self.show_next_step, width=10, state=tk.DISABLED)
        self.next_step_button.grid(row=0, column=2, padx=5)

        # Status label
        self.status_label = tk.Label(self.main_frame, text="Moves: 0", font=('Arial', 12))
        self.status_label.pack(pady=10)

        # Start a new game
        self.new_game()

    def new_game(self):
        # Generate a random solvable board
        self.current_state = self.generate_solvable_board()
        self.moves_count = 0
        self.solution_steps = []
        self.step_index = 0
        self.update_ui()
        self.next_step_button.config(state=tk.DISABLED)

    def generate_solvable_board(self):
        # Start with the goal state
        board = copy.deepcopy(self.goal_state)

        # Perform random moves to shuffle the board (ensures solvability)
        current = PuzzleState(board)
        for _ in range(50):  # 50 random moves should be sufficient
            neighbors = current.get_neighbors()
            if neighbors:
                current = random.choice(neighbors)

        return current.board

    def update_ui(self):
        for i in range(3):
            for j in range(3):
                value = self.current_state[i][j]
                if value == 0:
                    self.grid_buttons[i][j].config(text="", state=tk.DISABLED, bg="lightgray")
                else:
                    self.grid_buttons[i][j].config(text=str(value), state=tk.NORMAL, bg="white")

        self.status_label.config(text=f"Moves: {self.moves_count}")

        # Check if the puzzle is solved
        if self.current_state == self.goal_state:
            messagebox.showinfo("Congratulations!", f"You solved the puzzle in {self.moves_count} moves!")

    def move_tile(self, i, j):
        # Find the blank position
        blank_i, blank_j = None, None
        for r in range(3):
            for c in range(3):
                if self.current_state[r][c] == 0:
                    blank_i, blank_j = r, c
                    break

        # Check if the clicked tile is adjacent to the blank space
        if (abs(i - blank_i) == 1 and j == blank_j) or (abs(j - blank_j) == 1 and i == blank_i):
            # Swap the tiles
            self.current_state[blank_i][blank_j], self.current_state[i][j] = \
                self.current_state[i][j], self.current_state[blank_i][blank_j]

            self.moves_count += 1
            self.update_ui()

    def is_solvable(self, board):
        # Flatten the board
        flat_board = [num for row in board for num in row if num != 0]

        # Count inversions
        inversions = 0
        for i in range(len(flat_board)):
            for j in range(i + 1, len(flat_board)):
                if flat_board[i] > flat_board[j]:
                    inversions += 1

        # For a 3x3 board, the puzzle is solvable if the number of inversions is even
        return inversions % 2 == 0

    def solve_puzzle(self):
        # Solve using A* algorithm
        initial_state = PuzzleState(self.current_state)
        goal_state = PuzzleState(self.goal_state)

        solution = self.a_star_search(initial_state, goal_state)

        if solution:
            self.solution_steps = solution
            self.step_index = 0
            self.next_step_button.config(state=tk.NORMAL)
            messagebox.showinfo("Solution Found", f"Solution found in {len(solution) - 1} steps!")
        else:
            messagebox.showerror("Error", "No solution found!")

    def a_star_search(self, initial_state, goal_state):
        git
        remote
        show
        origin        frontier = []
        heapq.heappush(frontier, (self.calculate_heuristic(initial_state), 0, initial_state))

        visited = set()
        g_score = {initial_state.hash: 0}

        step_counter = 0

        while frontier:
            _, _, current = heapq.heappop(frontier)

            if current.board == goal_state.board:
                return self.reconstruct_path(current)
            visited.add(current.hash)

            for neighbor in current.get_neighbors():
                if neighbor.hash in visited:
                    continue

                tentative_g_score = g_score[current.hash] + 1

                if neighbor.hash not in g_score or tentative_g_score < g_score[neighbor.hash]:
                    g_score[neighbor.hash] = tentative_g_score
                    f_score = tentative_g_score + self.calculate_heuristic(neighbor)
                    heapq.heappush(frontier, (f_score, step_counter, neighbor))
                    step_counter += 1

        return None

    def calculate_heuristic(self, state):
        # Manhattan distance heuristic
        total_distance = 0
        for i in range(3):
            for j in range(3):
                value = state.board[i][j]
                if value != 0:
                    # Find where this value should be in the goal state
                    goal_i, goal_j = (value - 1) // 3, (value - 1) % 3
                    total_distance += abs(i - goal_i) + abs(j - goal_j)
        return total_distance

    def reconstruct_path(self, state):
        path = []
        current = state
        while current:
            path.append(current.board)
            current = current.parent
        return path[::-1]  # Reverse to get the path from start to goal

    def show_next_step(self):
        if self.step_index < len(self.solution_steps) - 1:
            self.step_index += 1
            self.current_state = self.solution_steps[self.step_index]
            self.moves_count += 1
            self.update_ui()

            if self.step_index == len(self.solution_steps) - 1:
                self.next_step_button.config(state=tk.DISABLED)


if __name__ == "__main__":
    root = tk.Tk()
    app = EightPuzzleGame(root)
    root.mainloop()