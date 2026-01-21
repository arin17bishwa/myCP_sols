from typing import List


class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        arr = nums

        def func(n: int) -> int:
            res = -1
            d = 1
            while n & d:
                res = n - d
                d <<= 1
            return res

        return [func(i) for i in arr]
