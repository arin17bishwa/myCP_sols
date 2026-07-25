from functools import cache


class Solution:

    def maxDotProduct(self, a: list[int], b: list[int]):

        @cache
        def func(i: int, j: int) -> int:
            nonlocal a, b
            if j < 0:
                return 0
            if i < 0:
                return -(1 << 62)

            return max(a[i] * b[j] + func(i - 1, j - 1), func(i - 1, j))

        return func(len(a) - 1, len(b) - 1)
