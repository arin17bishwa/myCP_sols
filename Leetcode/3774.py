from typing import List


class Solution:
    def absDifference(self, nums: List[int], k: int) -> int:
        arr = nums
        arr.sort()

        return abs(sum(arr[-k:]) - sum(arr[:k]))
