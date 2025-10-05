from typing import List


class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        return sum(nums[i] for i in range(0, len(nums), 2)) - sum(
            nums[i] for i in range(1, len(nums), 2)
        )
