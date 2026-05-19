from typing import List


class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        return min(set(nums1).intersection(set(nums2)), default=-1)
