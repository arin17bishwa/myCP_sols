from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        q = deque()

        def find_neighbours(x: int, y: int):
            diff = [[1, 0], [0, 1], [-1, 0], [0, -1]]

            for dx, dy in diff:
                _x, _y = x + dx, y + dy
                if 0 <= _x < m and 0 <= _y < n:
                    yield _x, _y

        vis: set[tuple[int, int]] = set()
        elapsed_time = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j))
                    vis.add((i, j))

        while q:
            for _ in range(len(q)):
                curr = q.popleft()
                for neighbour in find_neighbours(*curr):
                    if neighbour not in vis and grid[neighbour[0]][neighbour[1]] == 1:
                        q.append(neighbour)
                        grid[neighbour[0]][neighbour[1]] = 2
                        vis.add(neighbour)

            elapsed_time += 1

        return -1 if any(1 in row for row in grid) else max(0, elapsed_time - 1)
