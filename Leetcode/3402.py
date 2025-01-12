from typing import List


class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        ans = 0
        m, n = len(grid), len(grid[0])

        for j in range(n):
            last_val = grid[0][j]

            for i in range(1, m):
                new_val = max(grid[i][j], last_val + 1)
                ans += new_val - grid[i][j]
                last_val = new_val
        return ans
