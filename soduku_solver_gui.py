import tkinter as tk
from tkinter import messagebox
# Import your solver and initial board
from sudoku_solver import solve_sudoku, initial_board


class SudokuGUI:
    def __init__(self, root, initial_board):
        self.root = root
        self.root.title("Sudoku Solver")
        self.cells = [[None for _ in range(9)] for _ in range(9)]
        self.create_widgets(initial_board)

    def create_widgets(self, initial_board):
        for row in range(9):
            for col in range(9):
                self.cells[row][col] = tk.Entry(self.root, width=3, font=(
                    'Arial', 18), borderwidth=2, relief="groove", justify='center')
                self.cells[row][col].grid(row=row, column=col, padx=5, pady=5)
                if initial_board[row][col] != ".":
                    self.cells[row][col].insert(0, initial_board[row][col])
                    # Disable editing of initial cells
                    self.cells[row][col].config(state='disabled')

        solve_button = tk.Button(self.root, text="Solve", command=self.solve)
        solve_button.grid(row=9, column=4, columnspan=1)

    def read_board(self):
        board = []
        for row in range(9):
            board_row = []
            for col in range(9):
                val = self.cells[row][col].get()
                if val == '':
                    board_row.append(".")
                else:
                    board_row.append(val)
            board.append(board_row)
        return board

    def solve(self):
        board = self.read_board()
        if solve_sudoku(board):
            self.update_board(board)
        else:
            messagebox.showinfo("Sudoku Solver", "No solution exists!")

    def update_board(self, board):
        for row in range(9):
            for col in range(9):
                # Only update cells that are editable
                if self.cells[row][col]['state'] == 'normal':
                    self.cells[row][col].delete(0, tk.END)
                    if board[row][col] != ".":
                        self.cells[row][col].insert(0, board[row][col])


if __name__ == "__main__":
    root = tk.Tk()
    app = SudokuGUI(root, initial_board)
    root.mainloop()
