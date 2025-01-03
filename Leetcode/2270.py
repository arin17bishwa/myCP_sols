from typing import List


class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        arr = nums
        n = len(arr)
        total = sum(arr)
        ans = curr = 0
        for i in range(n - 1):
            curr += arr[i]
            ans += curr * 2 >= total
        return ans
