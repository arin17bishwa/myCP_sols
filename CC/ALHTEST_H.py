from typing import *

from collections import deque


class Solution:
    def maximumMinutes(self, grid: List[List[int]]) -> int:
        arr = grid
        n, m = len(arr), len(arr[0])
        q = deque()
        vis = [[0] * m for _ in range(n)]
        fires = []
        walls = []
        for i in range(n):
            for j in range(m):
                if arr[i][j] == 1:
                    fires.append((i, j))
                elif arr[i][j] == 2:
                    walls.append((i, j))

        dr = (
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        )

        q.append((walls[0], walls[1], 1))
        for i, j in fires:
            q.append((i, j, 2))

        while q:
            x, y, tp = q.popleft()
            vis[x][y] = tp
            if (x, y) == (n - 1, m - 1):
                return 1

    def func(self, grid: List[List[int]]) -> int:
        arr = grid
        n, m = len(arr), len(arr[0])
        q = deque()
        vis = [[0] * m for _ in range(n)]
        fires = []
        walls = []
        for i in range(n):
            for j in range(m):
                if arr[i][j] == 1:
                    fires.append((i, j))
                elif arr[i][j] == 2:
                    walls.append((i, j))

        dr = (
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        )

        q.append((walls[0], walls[1], 1))
        for i, j in fires:
            q.append((i, j, 2))

        while q:
            x, y, tp = q.popleft()
            vis[x][y] = tp
            if (x, y) == (n - 1, m - 1):
                return 1

            for a, b in dr:
                nx = x + a
                ny = y + b
                if (0 <= nx < n and 0 <= ny < m) and ((tp == 1 and vis[nx][ny]) or (tp == 2 and vis[nx][ny] != 2)):
                    q.append((nx, ny, tp))


if __name__ == '__main__':
    pass
