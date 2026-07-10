from collections import deque


class Solution:
    def countCoordinates(self, mat: list[list[int]]) -> int:
        n, m = len(mat), len(mat[0])

        dirs: tuple[tuple[int, int], ...] = ((-1, 0), (1, 0), (0, -1), (0, 1))

        def is_valid(_x: int, _y: int) -> bool:
            return 0 <= _x < n and 0 <= _y < m

        def get_neighbours(_x: int, _y: int):
            for dx, dy in dirs:
                nx, ny = _x + dx, _y + dy
                if is_valid(nx, ny) and mat[_x][_y] <= mat[nx][ny]:
                    yield nx, ny

        def bfs(sources: list[tuple[int, int]]):
            vis: set[tuple[int, int]] = set()

            q: deque[tuple[int, int]] = deque(sources)

            while q:
                x, y = q.popleft()
                if (x, y) in vis:
                    continue
                else:
                    vis.add((x, y))

                for neighbour in get_neighbours(x, y):
                    if neighbour not in vis:
                        q.append(neighbour)

            return vis

        return len(
            bfs([(0, j) for j in range(m)] + [(i, 0) for i in range(n)])
            & bfs([(i, m - 1) for i in range(n)] + [(n - 1, j) for j in range(m)])
        )
