# sudoku_solver.py

initial_board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]


def print_sudoku(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("-" * 21)

        for j in range(len(board[i])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(board[i][j] + " ", end="")


def solve_sudoku(board):
    return helper(board, 0, 0)


def helper(board, row, col):
    if row == len(board):
        return True
    if col != 8:
        ncol = col + 1
        nrow = row
    else:
        nrow = row + 1
        ncol = 0

    if board[row][col] != ".":
        if helper(board, nrow, ncol):
            return True
    else:
        for i in range(len(board)):
            if issafe(board, row, col, i+1):
                board[row][col] = str(i+1)
                if helper(board, nrow, ncol):
                    return True
                else:
                    board[row][col] = "."
    return False


def issafe(board, row, col, number):
    # rows
    for i in range(len(board)):
        if board[row][i] == str(number):
            return False

    # columns
    for i in range(len(board)):
        if board[i][col] == str(number):
            return False

    # grids
    for i in range(row//3 * 3, row//3 * 3 + 3):
        for j in range(col//3 * 3, col//3 * 3 + 3):
            if board[i][j] == str(number):
                return False

    return True
