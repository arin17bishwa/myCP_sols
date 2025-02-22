from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        arr = nums
        n = len(arr)
        ans = end = far = 0

        for i in range(n - 1):
            far = max(far, arr[i] + i)
            if i == end:
                ans += 1
                end = far
        return ans
