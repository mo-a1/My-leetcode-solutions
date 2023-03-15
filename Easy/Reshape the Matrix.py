"""
In MATLAB, there is a handy function called reshape which can reshape an m x n matrix into a new one with a different
 size r x c keeping its original data.
You are given an m x n matrix mat and two integers r and c representing the number of rows and the number of columns of
 the wanted to be reshaped matrix.
The reshaped matrix should be filled with all the elements of the original matrix in the same row-traversing order
 as they were.
If the reshape operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise,
 output the original matrix.
"""
import itertools
from typing import List


def matrix_reshape(mat: List[List[int]], r: int, c: int) -> List[List[int]]:
    if r * c != len(mat) * len(mat[0]):
        return mat
    it = itertools.chain(*mat)
    return [list(itertools.islice(it, c)) for _ in range(r)]
