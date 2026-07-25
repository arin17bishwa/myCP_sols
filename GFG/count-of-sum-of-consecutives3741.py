class Solution:
    def getCount(self, n: int) -> int:
        ans: int = 0
        k: int = 2
        while True:
            x = (k * (k - 1)) >> 1
            if x >= n:
                break
            ans += (n - x) % k == 0
            k += 1
        return ans
