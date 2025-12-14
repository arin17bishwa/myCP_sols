class Solution:
    def prefixSum2D(self, mat: list[list[int]], queries: list[int]) -> list[int]:
        m, n = len(mat), len(mat[0])

        for j in range(1, n):
            mat[0][j] += mat[0][j - 1]
        for i in range(1, m):
            mat[i][0] += mat[i - 1][0]

        for i in range(1, m):
            for j in range(1, n):
                mat[i][j] += mat[i - 1][j] + mat[i][j - 1] - mat[i - 1][j - 1]

        ans = []
        for r1, c1, r2, c2 in queries:
            ans.append(
                mat[r2][c2]
                - (mat[r2][c1 - 1] * (c1 != 0))
                - (mat[r1 - 1][c2] * (r1 != 0))
                + (mat[r1 - 1][c1 - 1] * (r1 != 0 and c1 != 0))
            )
        return ans
