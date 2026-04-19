class Solution:
    def isPower(self, x: int, y: int) -> bool:
        if x == 1:
            return False
        while y % x == 0:
            y //= x
        return y == 1
