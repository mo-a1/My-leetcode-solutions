"""
You are given an m x n integer matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.
"""
from typing import List


def search_matrix(matrix: List[List[int]], target: int) -> bool:
    left = 0
    right = len(matrix) - 1
    while left <= right:
        mid = (left + right) // 2
        if target in matrix[mid]:
            return True
        elif target < matrix[mid][0]:
            right = mid - 1
        else:
            left = mid + 1
    return False
