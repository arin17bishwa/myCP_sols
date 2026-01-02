from collections import Counter
from typing import List


class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        arr = nums
        n = len(arr)
        freq = Counter(arr)
        mx = max(freq.values())
        if (mx << 1) <= n:
            return 1 if n & 1 else 0
        return (mx << 1) - n
