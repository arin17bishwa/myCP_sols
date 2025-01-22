from collections import deque
from typing import List


class Solution:

    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m, n = len(isWater), len(isWater[0])
        island_map = [[-1] * n for _ in range(m)]
        queue = deque()
        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    queue.append((i, j))
                    island_map[i][j] = 0

        def is_valid_index(p: int, q: int):
            return (0 <= p < m) and (0 <= q < n)

        current_height = 0
        while queue:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                if island_map[x][y] > 0:
                    continue
                elif island_map[x][y] == 0:
                    pass
                else:
                    island_map[x][y] = current_height

                for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                    new_x, new_y = x + dx, y + dy
                    if is_valid_index(new_x, new_y) and island_map[new_x][new_y] == -1:
                        queue.append((new_x, new_y))

            current_height += 1

        return island_map
