from typing import List
from itertools import chain


class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0

        for i in range(m - 2):
            for j in range(n - 2):
                ans += self.is_magic_square(
                    sub_grid=[
                        grid[i][j : j + 3],
                        grid[i + 1][j : j + 3],
                        grid[i + 2][j : j + 3],
                    ]
                )
        return ans

    @staticmethod
    def is_magic_square(sub_grid: List[List[int]]) -> bool:
        def col_sum(col_num: int) -> int:
            return sum(sub_grid[i][col_num] for i in range(n))

        n = 3
        row_sum_valid = sum(sub_grid[0]) == sum(sub_grid[1]) == sum(sub_grid[-1])
        col_sum_valid = col_sum(0) == col_sum(1) == col_sum(2)
        diagonal_sum_1 = sub_grid[0][0] + sub_grid[1][1] + sub_grid[2][2]
        diagonal_sum_2 = sub_grid[0][2] + sub_grid[1][1] + sub_grid[2][0]
        diagonal_sum_valid = diagonal_sum_1 == diagonal_sum_2
        return (
            all(all(1 <= i <= 9 for i in row) for row in sub_grid)
            and len(set(chain(*sub_grid))) == 9
            and row_sum_valid
            and col_sum_valid
            and diagonal_sum_valid
        )
