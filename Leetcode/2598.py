from collections import Counter
from typing import List


class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        arr = [i % value for i in nums]
        freq = Counter(arr)
        mn = [10**9, 10**9]
        for i in range(value):
            x = freq[i]
            if x == 0:
                return i
            elif x < mn[1]:
                mn = [i, x]
        return value * mn[1] + mn[0]


def main():
    obj = Solution()

    arr = [1, -10, 7, 13, 6, 8]
    k = 5

    arr = [1, -10, 7, 13, 6, 8]
    k = 7

    ans = obj.findSmallestInteger(arr, k)

    print(ans)


if __name__ == "__main__":
    main()
