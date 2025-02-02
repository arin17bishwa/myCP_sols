from collections import Counter


class Solution:
    def maxDifference(self, s: str) -> int:
        freq = Counter(s)
        return max(i for i in freq.values() if i & 1) - min(
            i for i in freq.values() if i & 1 == 0
        )
