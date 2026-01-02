from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        arr = nums
        freq = Counter(arr)
        return sorted(freq.keys(), key=lambda x: -freq[x])[:k]
