from typing import List


class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        arr = nums
        n = len(arr)
        left = 0
        right = sum(arr)
        ans = [0] * n

        for idx, ele in enumerate(arr):
            right -= ele
            ans[idx] = abs(right - left)
            left += ele
        return ans
