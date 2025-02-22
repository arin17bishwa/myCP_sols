from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        mx = 0
        for idx, val in enumerate(nums):
            if mx < idx:
                return False
            mx = max(mx, idx + val)

        return True
