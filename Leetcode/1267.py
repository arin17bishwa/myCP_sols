from collections import Counter
from typing import List


class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        row_counter = Counter()
        col_counter = Counter()
        m, n = len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    row_counter[i] += 1
                    col_counter[j] += 1

        ans = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] and (row_counter[i] > 1 or col_counter[j] > 1):
                    ans += 1

        return ans
