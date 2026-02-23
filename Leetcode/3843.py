from collections import Counter
from typing import List


class Solution:
    def firstUniqueFreq(self, nums: List[int]) -> int:
        arr = nums
        freq = Counter(arr)
        freq_freq = Counter(freq.values())
        for i in arr:
            if freq_freq[freq[i]] == 1:
                return i
        return -1
