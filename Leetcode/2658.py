from typing import List


class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[0] * n for _ in range(m)]

        def is_visitable(x: int, y: int) -> bool:
            return m > x >= 0 and n > y >= 0 and grid[x][y] != 0 and visited[x][y] == 0

        def get_dirs(x: int, y: int):
            for dx, dy in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                if is_visitable(x + dx, y + dy):
                    yield x + dx, y + dy

        def dfs(x: int, y: int) -> int:
            visited[x][y] = 1
            curr = grid[x][y]
            for new_x, new_y in get_dirs(x, y):
                curr += dfs(new_x, new_y)
            return curr

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] and not visited[i][j]:
                    ans = max(ans, dfs(i, j))
        return ans
