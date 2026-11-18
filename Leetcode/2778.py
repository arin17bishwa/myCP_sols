from typing import List


class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        arr = nums
        n = len(arr)

        return sum(
            ele * ele if n % idx == 0 else 0 for idx, ele in enumerate(arr, start=1)
        )
