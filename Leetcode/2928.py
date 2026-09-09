class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        children: int = 3
        if children * limit < n:
            return 0
        ans: int = 0

        for i in range(1 + min(n, limit)):
            for j in range(1 + min(n, limit)):
                for k in range(1 + min(n, limit)):
                    ans += (i + j + k) == n

        return ans
