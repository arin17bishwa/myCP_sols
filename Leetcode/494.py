from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        arr = nums
        n = len(arr)
        ans: int = 0

        for mask in range(1 << n):
            curr: int = 0
            for i in range(n):
                if mask & (1 << i):
                    mul = 1
                else:
                    mul = -1
                curr += mul * arr[i]
            ans += curr == target

        return ans
