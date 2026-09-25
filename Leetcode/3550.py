from typing import List


class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for idx, ele in enumerate(nums):
            if idx == sum(map(int, str(ele))):
                return idx
        return -1
