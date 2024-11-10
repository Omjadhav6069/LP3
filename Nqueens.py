# Function to print the chessboard with Queens placed
def print_board(board):
    for row in board:
        print(" ".join(row))
    print()

# Check if placing a queen at board[row][col] is safe
def is_safe(board, row, col, n):
    # Check column
    for i in range(row):
        if board[i][col] == 'Q':
            return False

    # Check upper-left diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1

    # Check upper-right diagonal
    i, j = row, col
    while i >= 0 and j < n:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j += 1

    return True

# Recursive backtracking function to place queens
def solve_n_queens(board, row, n):
    # Base case: if all queens are placed
    if row == n:
        print_board(board)
        return True

    # Try placing a queen in each column of the current row
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 'Q'  # Place queen
            if solve_n_queens(board, row + 1, n):  # Recur to place next queen
                return True
            board[row][col] = '.'  # Backtrack if no solution found

    return False

# Set up the board and place the first queen at a specific position
def n_queens_with_first_placed(n, first_row=0, first_col=0):
    # Initialize board
    board = [['.' for _ in range(n)] for _ in range(n)]
    board[first_row][first_col] = 'Q'  # Place the first queen at the specified position

    # Start solving from the next row
    if not solve_n_queens(board, first_row + 1, n):
        print("No solution found")

# Example usage with n = 4 and first queen placed at (0, 1)
n_queens_with_first_placed(5, 3, 1)
