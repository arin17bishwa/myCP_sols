import heapq
from typing import List


class Solution:
    def minCost(self, m: int, n: int, waitCost: List[List[int]]) -> int:
        directions = [(1, 0), (0, 1)]
        heap = [(1, 0, 0, 1)]
        visited = [[[float("inf")] * 2 for _ in range(n)] for _ in range(m)]
        visited[0][0][1] = 1

        while heap:
            cost, i, j, par = heapq.heappop(heap)

            if i == m - 1 and j == n - 1:
                return cost

            if par == 1:
                for dx, dy in directions:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < m and 0 <= nj < n:
                        x = cost + (ni + 1) * (nj + 1)
                        if x < visited[ni][nj][0]:
                            visited[ni][nj][0] = x
                            heapq.heappush(heap, (x, ni, nj, 0))
            else:
                wait = waitCost[i][j]
                x = cost + wait
                if x < visited[i][j][1]:
                    visited[i][j][1] = x
                    heapq.heappush(heap, (x, i, j, 1))

        return -1
