from typing import List
from collections import Counter

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq=Counter(nums)
        mx=max(freq.values())
        return tuple(freq.values()).count(mx)*mx