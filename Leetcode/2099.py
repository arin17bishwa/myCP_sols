from collections import Counter
from typing import List


class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(sorted(nums, reverse=True)[:k])
        ans = []
        for i in nums:
            if freq[i]:
                ans.append(i)
                freq[i] -= 1
        return ans
