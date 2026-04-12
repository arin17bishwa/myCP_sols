class Solution:
    def isToeplitz(self, mat):
        m, n = len(mat), len(mat[0])

        for i in range(1, m):
            for j in range(1, n):
                if mat[i - 1][j - 1] != mat[i][j]:
                    return False
        return True
