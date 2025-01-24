from collections import defaultdict
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        freq = defaultdict(int)
        for i in nums:
            freq[i] += 1
            if freq[i] > 1:
                return True
        return False
