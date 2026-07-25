class Solution:
    def maximumSum(self, mat: list[list[int]], k: int) -> int:
        n = len(mat)
        # print(*mat, sep="\n")
        # print("-" * 30)

        for i in range(1, n):
            mat[0][i] += mat[0][i - 1]
            mat[i][0] += mat[i - 1][0]

        for i in range(1, n):
            for j in range(1, n):
                mat[i][j] += mat[i - 1][j] + mat[i][j - 1] - mat[i - 1][j - 1]

        ans = mat[k - 1][k - 1]

        for i in range(k - 1, n):
            for j in range(k - 1, n):
                ans = max(
                    ans,
                    mat[i][j]
                    - (0 if i == k - 1 else mat[i - k][j])
                    - (0 if j == k - 1 else mat[i][j - k])
                    + (0 if (i == k - 1 or j == k - 1) else mat[i - k][j - k]),
                )

        # print(*mat, sep="\n")
        return ans
