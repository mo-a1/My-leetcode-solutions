"""
Given an integer numRows, return the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:-
# https://leetcode.com/problems/pascals-triangle/description/
"""
from typing import List


def generate(num_rows: int) -> List[List[int]]:
    p_tr = [[1 for _ in range(1, i + 1)] for i in range(num_rows + 1)]
    if len(p_tr) > 2:
        for row in range(2, len(p_tr)):
            for n in range(1, row - 1):
                p_tr[row][n] = p_tr[row - 1][n] + p_tr[row - 1][n - 1]
    del p_tr[0]
    return p_tr
