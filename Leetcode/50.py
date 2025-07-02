class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n

        ans = 1.0

        while n:
            if n & 1:
                ans *= x
                n -= 1
            else:
                x *= x
                n >>= 1
        return ans
