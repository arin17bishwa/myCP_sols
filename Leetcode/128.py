from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        arr = nums
        ans = 0
        there = set(arr)
        for i in there:
            if i - 1 in there:
                continue
            else:
                x = i
                curr = 1
                while x + 1 in there:
                    x += 1
                    curr += 1
                ans = max(ans, curr)
        return ans
