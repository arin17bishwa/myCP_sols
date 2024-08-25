from typing import List


class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
        self.matrix = rectangle

    def updateSubrectangle(
            self, row1: int, col1: int, row2: int, col2: int, new_value: int
    ) -> None:
        for i in range(row1, row2 + 1):
            for j in range(col1, col2 + 1):
                self.matrix[i][j] = new_value

    def getValue(self, row: int, col: int) -> int:
        return self.matrix[row][col]
