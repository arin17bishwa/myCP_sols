class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        full_rounds: int = time // (n - 1)
        rem: int = time % (n - 1)
        return 1 + rem if full_rounds % 2 == 0 else n - rem
