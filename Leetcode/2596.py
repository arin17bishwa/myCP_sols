from typing import List


class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        n = len(grid)
        if grid[0][0] != 0:
            return False
        arr = [[-1, -1] for _ in range(n * n)]
        for i in range(n):
            for j in range(n):
                arr[grid[i][j]] = [i, j]

        for i in range(1, len(arr)):
            prev_x, prev_y = arr[i - 1]
            x, y = arr[i]
            if (abs(prev_x - x), abs(prev_y - y)) not in ((1, 2), (2, 1)):
                return False
        return True
