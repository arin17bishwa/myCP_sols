from typing import List


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A: List[int]) -> int:
        arr = A
        n = len(arr)
        curr = 0
        ans = arr[0]
        for i in arr:
            curr += i
            ans = max(ans, curr)
            curr = max(0, curr)
        return ans
