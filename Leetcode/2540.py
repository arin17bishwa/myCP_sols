from typing import List


class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        i = j = 0

        while i < m and j < n:
            a, b = nums1[i], nums2[j]
            if a == b:
                return a
            elif a < b:
                i += 1
            else:
                j += 1
        return -1
