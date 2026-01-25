from functools import cache


class Solution:
    def findWays(self, n: int) -> int:
        if n & 1:
            return 0

        @cache
        def func(k: int) -> int:
            if k <= 1:
                return 1
            res = 0
            for i in range(k):
                res += func(i) * func(k - 1 - i)

            return res

        return func(n >> 1)


def main():
    obj = Solution()

    n = 8

    ans = obj.findWays(n)

    # print(ans)


if __name__ == "__main__":
    main()
