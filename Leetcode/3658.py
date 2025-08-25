from math import gcd


class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        return gcd(
            sum(i for i in range(0, 2 * n + 1, 2)),
            sum(i for i in range(1, 2 * n + 1, 2)),
        )
