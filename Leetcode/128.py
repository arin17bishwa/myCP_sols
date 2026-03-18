from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        there = set(nums)
        for i in there:
            if i - 1 in there:
                continue
            else:
                x = i
                while x + 1 in there:
                    x += 1
                ans = max(ans, x - i + 1)
        return ans
