from typing import List


class Solution:
    def evenNumberBitwiseORs(self, nums: List[int]) -> int:
        ans = 0
        for i in nums:
            if i % 2 == 0:
                ans |= i
        return ans
