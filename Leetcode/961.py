from collections import Counter
from typing import List


class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums) >> 1
        for k, v in Counter(nums).items():
            if v == n:
                return k
        return -1
