from collections import deque

MAX = 10**9


class Solution:
    def nearest(self, grid: list[list[int]]) -> list[list[int]]:
        n, m = len(grid), len(grid[0])

        def get_neighbours(x: int, y: int):
            dirs = [
                [0, 1],
                [0, -1],
                [1, 0],
                [-1, 0],
                # [1,1],
                # [1,-1],
                # [-1,1],
                # [-1,-1]
            ]

            for dx, dy in dirs:
                _x, _y = x + dx, y + dy
                if 0 <= _x < n and 0 <= _y < m:
                    yield _x, _y

        q: deque[tuple[int, int]] = deque()
        ans = [[MAX] * m for _ in range(n)]
        vis = [[0] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    q.append((i, j))
                    vis[i][j]=1
        dist = 0

        while q:

            for _ in range(len(q)):
                i, j = q.popleft()
                ans[i][j] = min(ans[i][j], dist)
                # vis[i][j] = 1

                for _i, _j in get_neighbours(i, j):
                    if vis[_i][_j]:
                        continue
                    q.append((_i, _j))
                    vis[_i][_j]=1

            dist += 1

        return ans


def main():
    obj = Solution()

    grid = [[0, 1, 1, 0], [1, 1, 0, 0], [0, 0, 1, 1]]
    grid = [[1, 0, 1], [1, 1, 0], [1, 0, 0]]

    ans = obj.nearest(grid)

    print(ans)


if __name__ == "__main__":
    main()
