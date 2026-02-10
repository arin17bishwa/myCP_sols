from collections import defaultdict
from typing import List


class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        arr = nums
        n = len(arr)
        for i in range(n, -1, -1):
            if self.is_possible(arr, i):
                return i
        return 0

    @staticmethod
    def is_possible(arr: list[int], k: int) -> bool:
        n = len(arr)
        odds = defaultdict(int)
        evens = defaultdict(int)
        for i in range(k):
            if arr[i] & 1:
                odds[arr[i]] += 1
            else:
                evens[arr[i]] += 1

        if len(odds) == len(evens):
            return True

        def alter_cnt(p: int, delta: int = 1):
            nonlocal evens, odds
            mp = odds if p & 1 else evens
            mp[p] += delta
            if mp[p] == 0:
                mp.pop(p)

        for i in range(k, n):
            alter_cnt(arr[i - k], -1)
            alter_cnt(arr[i], 1)
            if len(odds) == len(evens):
                return True

        return False


def main():
    obj = Solution()

    arr = [2, 5, 4, 3]
    arr = [3, 2, 2, 5, 4]
    arr = [1, 2, 3, 2]

    ans = obj.longestBalanced(arr)

    print(ans)


if __name__ == "__main__":
    main()
