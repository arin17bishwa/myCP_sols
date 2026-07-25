from typing import List


class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        m, n = len(mat), len(mat[0])

        for i in range(m):
            diff = (k % n) * (1 if i & 1 else -1)
            for j in range(n):
                if mat[i][(j + diff) % n] != mat[i][j]:
                    return False
        return True
