from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr = nums
        n = len(arr)
        ans = arr[:]
        curr = arr[-1]

        for i in range(1, n - 1):
            ans[i] *= ans[i - 1]
        ans[-1] = ans[-2]

        for i in range(n - 2, 0, -1):
            ans[i] = ans[i - 1] * curr
            curr *= arr[i]

        ans[0] = curr
        return ans
