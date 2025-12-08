from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        arr = nums
        curr = ans = 0
        for i in arr:
            if i:
                curr += 1
            else:
                ans = max(curr, ans)
                curr = 0
        return max(ans, curr)
