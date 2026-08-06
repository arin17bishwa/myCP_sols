class Solution:
    def hammingWeight(self, n: int) -> int:
        ans: int = 0
        while n:
            ans += n & 1
            n >>= 1
        return ans
