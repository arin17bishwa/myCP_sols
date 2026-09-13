from functools import reduce


class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def prod_digits(k: int) -> int:
            return reduce(lambda x, y: x * y, map(int, str(k)), 1)

        while prod_digits(n) % t != 0:
            n += 1
        return n
