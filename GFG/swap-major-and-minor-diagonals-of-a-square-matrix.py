class Solution:
    def swapDiagonal(self, mat: list[list[int]]) -> None:
        n = len(mat)
        for i in range(n):
            mat[i][i], mat[i][n - 1 - i] = mat[i][n - 1 - i], mat[i][i]
