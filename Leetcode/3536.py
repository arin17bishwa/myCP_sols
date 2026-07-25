class Solution:
    def maxProduct(self, n: int) -> int:
        digs = list(map(int, str(n)))
        m = len(digs)
        ans = 0
        for i in range(m - 1):
            for j in range(i + 1, m):
                ans = max(ans, digs[i] * digs[j])

        return ans
