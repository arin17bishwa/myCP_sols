from functools import cache
from math import factorial


class Solution:
    def countBSTs(self, arr: list[int]) -> list[int]:
        n = len(arr)
        ans = [0] * n
        for i, idx in enumerate(sorted(range(n), key=lambda x: arr[x])):
            ans[idx] = self.catalan_number(i) * self.catalan_number(n - (i + 1))
        return ans

    @cache
    def catalan_number(self, i: int) -> int:
        return factorial(2 * i) // (factorial(i) * factorial(i + 1))


def main():
    obj = Solution()

    arr = [2, 1, 3]
    arr = [13, 6, 15, 3, 2]

    # ans = obj.countBSTs(arr)
    # print(ans)


if __name__ == "__main__":

    main()
