from typing import List


class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        arr = nums
        n = len(arr)
        ans = 0

        for idx, ele in enumerate(arr, start=1):
            if n % idx == 0:
                ans += ele * ele
        return ans
