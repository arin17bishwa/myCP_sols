from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        arr = nums
        ans = nums[0]
        curr = 0
        for i in arr:
            curr = max(i, curr + i)
            ans = max(ans, curr)
        return ans
