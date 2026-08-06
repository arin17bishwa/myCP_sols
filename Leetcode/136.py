from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans: int = 0
        for i in nums:
            ans ^= i
        return ans
