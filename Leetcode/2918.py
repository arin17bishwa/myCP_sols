from typing import List


class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        z1, z2 = nums1.count(0), nums2.count(0)
        s1, s2 = sum(nums1), sum(nums2)

        if z1 == z2 == 0:
            return s1 if s1 == s2 else -1
        elif z1 == 0:
            return s1 if s1 >= s2 + z2 else -1
        elif z2 == 0:
            return s2 if s1 + z1 <= s2 else -1
        return max(s1 + z1, s2 + z2)
