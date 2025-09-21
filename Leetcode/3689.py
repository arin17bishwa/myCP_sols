from typing import List


class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        arr = nums
        mx, mn = max(arr), min(arr)
        return k * (mx - mn)
