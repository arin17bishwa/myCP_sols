from collections import Counter
from typing import List


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        arr = nums
        freq = Counter(arr)
        if k == 0:
            return sum(v > 1 for v in freq.values())
        ans = 0
        for key in freq:
            if key + k in freq:
                ans += 1
        return ans
