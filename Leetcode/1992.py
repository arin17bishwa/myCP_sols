from typing import List


class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        ans: List[List[int]] = []
        end: List[int] = []
        m, n = len(land), len(land[0])
        dirs = [[0, 1], [1, 0]]

        def get_ele(_x, _y):
            if not (0 <= _x < m and 0 <= _y < n):
                return -1
            return land[_x][_y]

        def set_ele(_x, _y, v=-1):
            if not (0 <= _x < m and 0 <= _y < n):
                return -1
            land[_x][_y] = v
            return land[_x][_y]

        def dfs(x, y):
            nonlocal land, end
            if get_ele(x, y) != 1:
                return
            set_ele(x, y, -1)
            end = max(end, [x, y])

            for dx, dy in dirs:
                dfs(x + dx, y + dy)

        for i in range(m):
            for j in range(n):
                if get_ele(i, j) == 1:
                    end = [i, j]
                    dfs(i, j)
                    ans.append([i, j] + end)
        return ans
