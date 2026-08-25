from typing import List


class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        s = set(nums)

        for i in range(1, 255):
            if k * i not in s:
                return k * i

        return -1
