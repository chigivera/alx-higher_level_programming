#!/usr/bin/python3
"""N queens puzzle solution finder."""
import sys


def is_safe(board, row, col, n):
    """Check if a queen can be placed on board[row][col]."""
    # Check this row on left side
    for j in range(col):
        if board[row][j] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(board, col, n):
    """Solve N queens puzzle using backtracking."""
    if col >= n:
        print_solution(board, n)
        return

    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            solve_nqueens(board, col + 1, n)
            board[i][col] = 0


def print_solution(board, n):
    """Print the coordinates of queens."""
    solution = []
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                solution.append([i, j])
    print(solution)


def main():
    """Main function to solve N queens puzzle."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for x in range(n)] for y in range(n)]
    solve_nqueens(board, 0, n)


if __name__ == "__main__":
    main()