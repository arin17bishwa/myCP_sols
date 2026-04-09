from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.m = len(matrix)
        self.n = len(matrix[0])
        self.prefix_sum = [i[:] for i in matrix]
        self.pre_process()

    def pre_process(self):
        for j in range(1, self.n):
            self.prefix_sum[0][j] += self.prefix_sum[0][j - 1]

        for i in range(1, self.m):
            self.prefix_sum[i][0] += self.prefix_sum[i - 1][0]

        for i in range(1, self.m):
            for j in range(1, self.n):
                self.prefix_sum[i][j] += (
                    self.prefix_sum[i - 1][j]
                    + self.prefix_sum[i][j - 1]
                    - self.prefix_sum[i - 1][j - 1]
                )

    def _sum_of_region(self, r: int, c: int) -> int:
        if r < 0 or c < 0:
            return 0
        return self.prefix_sum[r][c]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (
            self._sum_of_region(row2, col2)
            - self._sum_of_region(row1 - 1, col2)
            - self._sum_of_region(row2, col1 - 1)
            + self._sum_of_region(row1 - 1, col1 - 1)
        )


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
