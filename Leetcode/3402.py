from typing import List


class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0
        for j in range(n):
            last = grid[0][j] - 1
            for i in range(m):
                req = max(last + 1, grid[i][j])
                ans += abs(grid[i][j] - req)
                last = req
        return ans
