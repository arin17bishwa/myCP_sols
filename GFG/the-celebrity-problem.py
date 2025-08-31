class Solution:
    def celebrity(self, mat: list[list[int]]) -> int:
        n = len(mat)
        for idx, row in enumerate(mat):
            if sum(row) == 1 and row.index(1) == idx:
                if all(mat[i][idx] == 1 for i in range(n)):
                    return idx
        return -1
