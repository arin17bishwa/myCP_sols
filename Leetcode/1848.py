from typing import List


class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        arr = nums
        n = len(arr)
        ans = n
        for i in range(n):
            if arr[i] == target:
                ans = min(ans, abs(start - i))
        return ans
