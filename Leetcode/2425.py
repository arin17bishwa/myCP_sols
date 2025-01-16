from collections import Counter
from typing import List


class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        counter = Counter()
        for a in nums1:
            counter[a] += n
        for b in nums2:
            counter[b] += m

        ans = 0
        for k, v in counter.items():
            if v & 1:
                ans ^= k
        return ans
