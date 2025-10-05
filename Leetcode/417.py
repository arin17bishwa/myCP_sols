from collections import deque
from typing import List, Any, Generator


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])

        def find_neighbours(x: int, y: int) -> Generator[tuple[int, int], Any, None]:
            directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

            for dx, dy in directions:
                if (0 <= x + dx < m) and (0 <= y + dy < n):
                    yield x + dx, y + dy

        def bfs(initial_borders: list[list[int]]) -> list[list[int]]:
            vis = [[0] * n for _ in range(m)]
            for i, j in initial_borders:
                vis[i][j] = 1

            q = deque(initial_borders)

            while q:
                x, y = q.popleft()
                vis[x][y] = 1
                for _x, _y in find_neighbours(x, y):
                    if (not vis[_x][_y]) and (heights[_x][_y] >= heights[x][y]):
                        q.append([_x, _y])
            return vis

        pacific_borders = [[0, j] for j in range(n)] + [[i, 0] for i in range(1, m)]
        atlantic_borders = [[m - 1, j] for j in range(n)] + [
            [i, n - 1] for i in range(m - 1)
        ]

        vis_pacific = bfs(pacific_borders)
        vis_atlantic = bfs(atlantic_borders)

        ans: list[list[int]] = []
        for i in range(m):
            for j in range(n):
                if vis_pacific[i][j] and vis_atlantic[i][j]:
                    ans.append([i, j])
        return ans
