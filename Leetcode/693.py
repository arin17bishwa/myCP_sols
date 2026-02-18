class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        if n < 3:
            return True
        while n > 1:
            if (n & 1) ^ ((n >> 1) & 1) == 0:
                return False
            n >>= 1
        return True
