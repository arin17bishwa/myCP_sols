from typing import List, Set, Tuple


class Solution:
    def isWordExist(self, mat: List[List[str]], word: str) -> bool:
        m, n = len(mat), len(mat[0])
        vis: Set[Tuple[int, int]] = set()

        def is_visitable_neighbour(x: int, y: int) -> bool:
            return (0 <= x < m and 0 <= y < n) and ((x, y) not in vis)

        def dfs(x: int, y: int, curr_idx: int) -> bool:
            if curr_idx == len(word) - 1:
                if word[curr_idx] == mat[x][y]:
                    return True
            if word[curr_idx] != mat[x][y]:
                return False
            vis.add((x, y))
            for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                _x, _y = x + dx, y + dy
                if is_visitable_neighbour(_x, _y):
                    possible = dfs(_x, _y, curr_idx + 1)
                    if possible:
                        return True
            vis.remove((x, y))
            return False

        for i in range(m):
            for j in range(n):
                if mat[i][j] == word[0]:
                    ans = dfs(i, j, 0)
                    if ans:
                        return True

        return False
