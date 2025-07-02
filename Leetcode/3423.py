from typing import List


class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        return max(
            max(abs(nums[i + 1] - nums[i]) for i in range(len(nums) - 1)),
            abs(nums[0] - nums[-1]),
        )
