from collections import Counter
from typing import List


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        freq = Counter(nums)
        ans = 0
        for k, v in freq.items():
            if freq[k - 1]:
                ans = max(ans, v + freq[k - 1])
        return ans
