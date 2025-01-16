from typing import List


class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        ans = 0
        if n & 1:
            for a in nums1:
                ans ^= a
        if m & 1:
            for b in nums2:
                ans ^= b

        return ans
