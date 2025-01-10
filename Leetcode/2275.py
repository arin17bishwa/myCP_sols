from collections import Counter
from typing import List


class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        freq = Counter()

        for candidate in candidates:
            pos = 0
            while candidate:
                if candidate & 1:
                    freq[pos] += 1
                candidate >>= 1
                pos += 1

        return max(freq.values())
