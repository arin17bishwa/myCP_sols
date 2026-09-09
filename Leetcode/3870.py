class Solution:
    def countCommas(self, n: int) -> int:
        return (n > 999) * (999 - n)
