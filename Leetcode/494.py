from functools import cache
from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        arr = nums
        n = len(arr)

        @cache
        def func(sub_target: int, start: int = 0) -> int:
            if start == n - 1:
                return (arr[-1], -arr[-1]).count(sub_target)
            curr = arr[start]
            ways = func(sub_target - curr, start + 1) + func(
                sub_target + curr, start + 1
            )
            return ways

        return int(func(target, 0))
