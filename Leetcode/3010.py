from typing import List


class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        arr = nums
        return arr[0] + sum(sorted(arr[1:])[:2])
