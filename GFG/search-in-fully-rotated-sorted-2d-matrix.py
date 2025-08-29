class Solution:
    def searchMatrix(self, mat: list[list[int]], x: int) -> bool:
        return any(x in row for row in mat)
