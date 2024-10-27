from typing import List
from collections import defaultdict


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = defaultdict(int)
        ans = 0

        def func(r: int, c: int) -> int:
            if (not 0 <= r < m) or (not 0 <= c < n) or (matrix[r][c] == 0):
                return 0
            if (r, c) in dp:
                return dp[(r, c)]

            dp[(r, c)] = 1 + min(
                func(r + 1, c),
                func(r + 1, c + 1),
                func(r, c + 1),
            )

            return dp[(r, c)]

        for i in range(m):
            for j in range(n):
                ans += func(i, j)

        return ans
