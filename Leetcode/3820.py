from collections import deque
from typing import List


class Solution:
    def specialNodes(
        self, n: int, edges: List[List[int]], x: int, y: int, z: int
    ) -> int:
        adj = [[] for _ in range(n)]
        for _u, _v in edges:
            adj[_u].append(_v)
            adj[_v].append(_u)

        def bfs(start):
            nonlocal adj
            dist = [-1] * n
            q = deque([start])
            dist[start] = 0

            while q:
                u = q.popleft()
                for v in adj[u]:
                    if dist[v] == -1:
                        dist[v] = dist[u] + 1
                        q.append(v)
            return dist

        dx = bfs(x)
        dy = bfs(y)
        dz = bfs(z)

        n = len(dx)
        ans = 0

        for a, b, c in zip(dx, dy, dz):
            a, b, c = sorted([a, b, c])

            if a * a + b * b == c * c:
                ans += 1
        return ans


def main():
    obj = Solution()

    n = 4
    arr = [[0, 1], [0, 2], [0, 3]]
    x, y, z = 1, 2, 3

    n = 4
    arr = [[0, 1], [1, 2], [2, 3]]
    x, y, z = 0, 3, 2

    n = 4
    arr = [[0, 1], [1, 2], [1, 3]]
    x, y, z = 1, 3, 0

    ans = obj.specialNodes(n, arr, x, y, z)

    print(ans)


if __name__ == "__main__":
    main()
