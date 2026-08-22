from math import prod


class Solution:
    def checkDivisibility(self, n: int) -> bool:
        digits = list(map(int, str(n)))
        sm = sum(digits)
        prd = prod(digits)
        return n % (sm + prd) == 0
