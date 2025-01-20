from typing import List, Tuple


class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])

        indices: List[Tuple[int, int]] = [(0, 0)] * (m * n + 2)
        for i in range(m):
            for j in range(n):
                indices[mat[i][j]] = (i, j)

        row_freq = [0] * m
        column_freq = [0] * n

        for idx, x in enumerate(arr):
            i, j = indices[x]
            row_freq[i] += 1
            column_freq[j] += 1
            if row_freq[i] == n or column_freq[j] == m:
                return idx
