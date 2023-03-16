"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.

"""
from typing import List


def is_valid_sudoku(board: List[List[str]]) -> bool:
    mem = []  # memory to check columns and sub-boxes
    mem2 = []  # memory to check rows only
    # check rows and columns
    for row in range(9):
        for column in range(9):
            if board[column][row] != ".":
                mem.append(board[column][row])  # to check columns
            if board[row][column] != ".":
                mem2.append(board[row][column])  # to check rows
        if len(mem) != len(set(mem)) or len(mem2) != len(set(mem2)):
            return False
        mem.clear()
        mem2.clear()
    # check sub-boxes
    for row in [0, 3, 6]:
        for column in [0, 3, 6]:
            for r in range(3):
                for c in range(3):
                    if board[row + r][column + c] != ".":
                        mem.append(board[row + r][column + c])
            if len(mem) != len(set(mem)):
                return False
            mem.clear()
    return True


print(is_valid_sudoku([[".", ".", "4", ".", ".", ".", "6", "3", "."], [".", ".", ".", ".", ".", ".", ".", ".", "."],
                       ["5", ".", ".", ".", ".", ".", ".", "9", "."], [".", ".", ".", "5", "6", ".", ".", ".", "."],
                       ["4", ".", "3", ".", ".", ".", ".", ".", "1"], [".", ".", ".", "7", ".", ".", ".", ".", "."],
                       [".", ".", ".", "5", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", ".", "."],
                       [".", ".", ".", ".", ".", ".", ".", ".", "."]]))  # correct is False
