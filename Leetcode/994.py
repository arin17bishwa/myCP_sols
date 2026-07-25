from collections import deque
from typing import List, Generator


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions: tuple[tuple[int, int], ...] = (
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1),
        )

        def is_valid(_x: int, _y: int) -> bool:
            nonlocal m, n
            return 0 <= _x < m and 0 <= _y < n

        def get_valid_neighbours(
            _x: int, _y: int
        ) -> Generator[tuple[int, int], None, None]:
            nonlocal directions

            for dx, dy in directions:
                if is_valid(_x + dx, _y + dy):
                    yield _x + dx, _y + dy

        d: deque[tuple[int, int]] = deque()
        fresh_count: int = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    d.append((i, j))
                elif grid[i][j] == 1:
                    fresh_count += 1

        if not d and fresh_count == 0:
            return 0

        ans: int = -1

        while d:
            for _ in range(len(d)):
                x, y = d.popleft()

                for nx, ny in get_valid_neighbours(x, y):
                    if grid[nx][ny] == 1:
                        d.append((nx, ny))
                        grid[nx][ny] = 2
                        fresh_count -= 1
            ans += 1

        return ans if fresh_count == 0 else -1
