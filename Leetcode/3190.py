from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        return sum(i % 3 != 0 for i in nums)
