from typing import List


class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        n = len(nums)
        prefix_min: list[int] = [nums[0]] * n

        for i in range(1, n):
            prefix_min[i] = min(prefix_min[i - 1], nums[i])

        return (
            -1
            if all(nums[i] == prefix_min[i] for i in range(n))
            else max(nums[i] - prefix_min[i] for i in range(n))
        )
