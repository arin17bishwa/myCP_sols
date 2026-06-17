from functools import cache


class Solution:
    def maxProduct(self, n: int) -> int:

        @cache
        def func(k: int) -> int:
            if k == 1:
                return 1
            return max(k, max(func(k - i) * func(i) for i in range(1, k)))

        return max(func(n - i) * func(i) for i in range(1, n))


def main():
    obj = Solution()

    n = 20

    ans = obj.maxProduct(n)

    print(ans)


if __name__ == "__main__":
    main()
