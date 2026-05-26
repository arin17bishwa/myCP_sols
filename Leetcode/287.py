from collections import Counter
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        freq = Counter(nums)
        for k, v in freq.items():
            if v > 1:
                return k
        return -1
