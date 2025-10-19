from typing import Any, Generator


class Solution:
    def knightTour(self, n: int) -> list[list[int]]:
        res: list[list[int]] = []
        ans = [[-1] * n for _ in range(n)]
        ans[0][0] = 0
        directions = (
            (1, 2),
            (2, 1),
            (-1, 2),
            (-2, 1),
            (1, -2),
            (2, -1),
            (-1, -2),
            (-2, -1),
        )

        def get_neighbours(x: int, y: int) -> Generator[tuple[int, int], Any, None]:
            nonlocal directions
            for dx, dy in directions:
                _x = x + dx
                _y = y + dy
                if 0 <= _x < n and 0 <= _y < n:
                    yield _x, _y

        def dfs(x: int = 0, y: int = 0, step: int = 0):
            nonlocal ans
            if step == n * n:
                raise

            for _x, _y in get_neighbours(x, y):
                if ans[_x][_y] == -1:
                    ans[_x][_y] = step
                    dfs(_x, _y, step + 1)
                    ans[_x][_y] = -1

        try:
            dfs(0, 0, 1)
        except Exception as _:
            res = ans
        return res
