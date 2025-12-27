from collections import Counter, defaultdict
from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        arr = nums
        freq = Counter(arr)
        sorted_keys = sorted(freq.keys())
        prefix_freq = defaultdict(int)
        prefix_freq[sorted_keys[0]] = freq[sorted_keys[0]]
        for i in range(1, len(sorted_keys)):
            prefix_freq[sorted_keys[i]] = (
                prefix_freq[sorted_keys[i - 1]] + freq[sorted_keys[i]]
            )
        return [prefix_freq[i] - freq[i] for i in arr]
