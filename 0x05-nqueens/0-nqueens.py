#!/usr/bin/python3
'''N queens puzzle
'''
import sys


solutions = []


def solve(row, dem, board):
    '''Solve the puzzle'''
    if (row == dem):
        solutions.append(
            [[r, board[r]] for r in range(dem)]
        )

    for col in range(dem):
        if isSafe(row, col, board):
            board.append(col)
            solve(row+1, dem, board)
            board.pop()


def isSafe(row, col, board):
    '''Check that there are no queen can attack other'''
    for r in range(row):
        if board[r] == col:
            return False
        if abs(r-row) == abs(board[r] - col):
            return False
    return True


def nqeens():
    '''Main point to start'''
    if len(sys.argv) != 2:
        print('Usage: nqueens N')
        sys.exit(1)
    try:
        dem = int(sys.argv[1])
    except Exception:
        print('N must be a number')
        sys.exit(1)

    if dem < 4:
        print('N must be at least 4')
        sys.exit(1)

    board = []
    r = 0
    solve(r, dem, board)
    for s in solutions:
        print(s)


if __name__ == '__main__':
    nqeens()
