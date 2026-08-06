from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans: int = 0
        arr = nums
        for i in arr:
            ans ^= i
        return ans
