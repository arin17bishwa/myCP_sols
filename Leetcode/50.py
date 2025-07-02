class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = 1

        for _ in range(abs(n)):
            if n > 0:
                ans *= x
            else:
                ans /= x
        return ans
