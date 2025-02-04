from collections import Counter
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        for k, v in Counter(nums).items():
            if v > len(nums) // 2:
                return k
