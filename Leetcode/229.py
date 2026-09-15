from collections import Counter
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> list[int]:
        freq = Counter(nums)
        return [k for k, v in freq.items() if v > len(nums) // 3]
