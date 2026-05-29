from typing import List


class Solution:
    def minElement(self, nums: List[int]) -> int:
        return min(sum(map(int, str(s))) for s in nums)
