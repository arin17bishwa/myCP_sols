class Solution:
    def countWays(self, n: int, m: int) -> int:
        mod = 10**9 + 7
        dp = [0] * (n + 1)

        for i in range(n + 1):
            if i < m:
                dp[i] = 1
            elif i == m:
                dp[i] = 2
            else:
                dp[i] = (dp[i - 1] + dp[i - m]) % mod
        return dp[-1]
