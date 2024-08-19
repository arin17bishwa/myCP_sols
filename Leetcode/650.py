class Solution:
    def minSteps(self, n: int) -> int:
        if n < 2:
            return 0
        dp = [n + 1] * (n + 1)
        dp[0] = dp[1] = 0
        dp[2] = 2
        for i in range(3, n + 1):
            for j in range(n // 2, 0, -1):
                if i % j == 0:
                    dp[i] = min(dp[i], dp[j] + (i // j))
        return dp[-1]
