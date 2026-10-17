"""
Generates sodoku games
"""

import random

N = 3
SIZE = N * N

# Given a Sudoku board board row, column, and the digit at that position, returns false if that digit is 
# already present in the row, column, or 3*3 block.
def is_valid(board, r, c, digit):
    # Is the digit already in this row?
    for col in range(SIZE):
        if board[r][col] == digit:
            return False

    # Is the board already in this column?
    for row in range(SIZE):
        if board[row][c] == digit:
            return False

    # Is the digit in this 3x3 block?
    box_top = r // N * N
    box_left = c // N * N
    for i in range(box_top, box_top + N):
        for j in range(box_left, box_left + N):
            if board[i][j] == digit:
                return False

    return True

def print_board(board):
    for r in range(len(board)):
        print(board[r])

# Recursive function used to fill the sudoku board with valid numbers
def fill(board, pos=0):
    if pos == SIZE * SIZE:          # past the last cell: board is complete
        return True

    r, c = divmod(pos, SIZE)        # cell number -> (row, column)
    
    if board[r][c] != 0:            # test if position has been filled, moves ahead if it has
        fill(board, pos + 1)
        return True

    digits = list(range(1, SIZE + 1))
    random.shuffle(digits)

    for d in digits:
        if is_valid(board, r, c, d):
            board[r][c] = d         # try it
            #print_board(board)
            #print("\n")

            if fill(board, pos + 1):    # can the rest of the board be filled?
                return True
            board[r][c] = 0         # no: undo and try the next digit
            #print("UNDO\n")

    return False                    # nothing fit: tell the previous cell to change


def main():
    board = [[0] * SIZE for _ in range(SIZE)]
    fill(board)
    print_board(board)


if __name__ == "__main__":
    main()