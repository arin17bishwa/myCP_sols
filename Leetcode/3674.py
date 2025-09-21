from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        return 0 if nums.count(nums[0]) == len(nums) else 1
