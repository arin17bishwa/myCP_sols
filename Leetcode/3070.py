from typing import List


class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        ans = int(grid[0][0] <= k)

        for j in range(1, n):
            grid[0][j] += grid[0][j - 1]
            ans += grid[0][j] <= k

        for i in range(1, m):
            grid[i][0] += grid[i - 1][0]
            ans += grid[i][0] <= k

        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += grid[i - 1][j] + grid[i][j - 1] - grid[i - 1][j - 1]
                ans += grid[i][j] <= k

        return ans
