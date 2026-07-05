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


def main():
    obj = Solution()

    a = [2, 3, 1, 7, 8]
    b = [3, 6, 7]

    a = [1, 2, 3]
    b = [4]

    a = [5, 8]
    b = [9, 1]

    ans = obj.maxDotProduct(a, b)

    # print(ans)

    return ans


if __name__ == "__main__":
    main()
