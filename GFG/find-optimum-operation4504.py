class Solution:
    def minOperation(self, n: int) -> int:
        ans: int = 0
        while n:
            if n & 1:
                n -= 1
            else:
                n >>= 1
            ans += 1
        return ans
