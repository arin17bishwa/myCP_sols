from typing import List


class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        arr = nums
        n = len(arr)
        ans = curr = arr[0]
        for i in range(1, n):
            if arr[i - 1] < arr[i]:
                curr += arr[i]
            else:
                curr = arr[i]
            ans = max(ans, curr)
        return ans
