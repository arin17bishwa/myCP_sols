from math import ceil
from typing import List


class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        arr = nums
        n = len(arr)
        ans: int = 0

        mn = arr[-1]

        for i in range(n - 2, -1, -1):
            if arr[i] <= mn:
                mn = arr[i]
                continue
            else:
                ops = ceil(arr[i] / mn)
                mn = arr[i] // ops
                ans += ops - 1
        return ans
