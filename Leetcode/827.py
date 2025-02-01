from typing import List


class DSU:
    def __init__(self, n: int):
        self.size = [1] * n
        self.parent = [i for i in range(n)]

    def find_parent(self, x: int) -> int:
        if x == self.parent[x]:
            return x
        self.parent[x] = self.find_parent(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        """return True if they are siblings"""
        parent_x = self.find_parent(x)
        parent_y = self.find_parent(y)
        if parent_x == parent_y:
            return True
        size_x = self.size[parent_x]
        size_y = self.size[parent_y]
        if size_x >= size_y:
            self.size[parent_x] += self.size[parent_y]
            self.parent[parent_y] = parent_x
        else:
            self.size[parent_y] += self.size[parent_x]
            self.parent[parent_x] = parent_y


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        index_mapping = {}
        curr_idx = 1
        for i in range(n):
            for j in range(n):
                index_mapping[(i, j)] = curr_idx
                curr_idx += 1

        dsu = DSU(n * n + 1)

        def is_valid_neighbour(x: int, y: int) -> bool:
            return 0 <= x < n and 0 <= y < n

        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        _x = i + dx
                        _y = j + dy
                        if is_valid_neighbour(_x, _y) and grid[_x][_y]:
                            dsu.union(index_mapping[(i, j)], index_mapping[(_x, _y)])
        ans = 1
        is_all_land = True
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    is_all_land = False
                    neighbour_parents = set()
                    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        _x, _y = i + dx, j + dy
                        if is_valid_neighbour(_x, _y) and grid[_x][_y]:
                            neighbour_parents.add(
                                dsu.find_parent(index_mapping[(_x, _y)])
                            )
                    ans = max(
                        ans, sum(dsu.size[parent] for parent in neighbour_parents) + 1
                    )

        return n * n if is_all_land else ans
