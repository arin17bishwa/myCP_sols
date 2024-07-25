from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])

        first_col_zero: bool = any((matrix[i][0] == 0 for i in range(m)))
        for idx, row in enumerate(matrix):
            if 0 in row:
                matrix[idx][0] = 0

        for j in range(1, n):
            matrix[0][j] = (
                0 if any((matrix[i][j] == 0 for i in range(m))) else matrix[0][j]
            )

        # now set to zeroes
        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(m):
                    matrix[i][j] = 0

        for i in range(m):
            if matrix[i][0] == 0:
                for j in range(n):
                    matrix[i][j] = 0
        if first_col_zero:
            for i in range(m):
                matrix[i][0] = 0
