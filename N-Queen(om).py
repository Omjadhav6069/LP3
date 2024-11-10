def is_safe(board, row, col, n):
    # Check this column on the current row
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_nqueens(board, row, n):
    # If all queens are placed, print the solution
    if row == n:
        print_board(board, n)
        return True
    
    # Try placing queens in all columns of the current row
    res = False
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col  # Place queen
            res = solve_nqueens(board, row + 1, n) or res
            # Backtrack
            board[row] = -1  # Reset the row (backtracking step)
    
    return res
def print_board(board, n):
    # Print the chessboard with queens placed
    for i in range(n):
        row = ['Q' if board[i] == j else '.' for j in range(n)]
        print(" ".join(row))
    print("\n")

def n_queens(n):
    board = [-1] * n  # Initialize the board with no queens placed
    # Place the first queen in a valid position (row 0, column 0)
    board[0] = 0
    print("Initial placement (First Queen in (0, 0)):\n")
    print_board(board, n)
    # Now place the remaining queens
    print("Solving N-Queens:\n")
    solve_nqueens(board, 1, n)

# Main program
if __name__ == "__main__":
    n = int(input("Enter the number of queens (n): "))
    n_queens(n)
