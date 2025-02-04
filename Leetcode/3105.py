from typing import List


class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        arr = nums
        n = len(arr)
        curr = ans = 1
        slope = 1  # 1 is increasing, -1 is decreasing

        for i in range(1, n):
            if slope * (arr[i] - arr[i - 1]) > 0:
                curr += 1
            else:
                slope *= -1
                curr = 1 if arr[i] == arr[i - 1] else 2
            ans = max(ans, curr)

        return ans
