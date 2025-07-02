from functools import cache


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n

        @cache
        def binary_exp(b: float, e: int):
            if e == 0:
                return 1
            if e == 1:
                return b

            if e & 1:
                return b * binary_exp(b, e - 1)
            else:
                t = binary_exp(b, e >> 1)
                return binary_exp(b, e >> 1) * binary_exp(b, e >> 1)

        return binary_exp(x, n)
