class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        return ((n + 1) >> 1) * (m >> 1) + (n >> 1) * ((m + 1) >> 1)
