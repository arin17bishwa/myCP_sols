from typing import List


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums[0])
        seen: set[int] = set(int(i, 2) for i in nums)
        for i in range(1 << 16):
            if i not in seen:
                return bin(i)[2:].zfill(n)
        return bin(1 << 16)
