from typing import List


class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        arr = nums
        pos = neg = 0
        for i in arr:
            if i > 0:
                pos += 1
            elif i < 0:
                neg += 1
        return max(pos, neg)
