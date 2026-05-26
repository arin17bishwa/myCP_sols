from collections import Counter
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for k, v in Counter(nums).items():
            if v > 1:
                return k
        return -1
