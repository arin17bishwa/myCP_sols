from functools import reduce
from typing import List


class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        arr = nums
        n = len(arr)
        if not any(arr):
            return 0
        return n if reduce(lambda x, y: x ^ y, arr, 0) else n - 1
