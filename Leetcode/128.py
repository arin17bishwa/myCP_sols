from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        arr = nums
        s: set[int] = set(arr)
        ans = 0

        for i in s:
            if i - 1 in s:
                continue
            else:
                j = i
                while j in s:
                    j += 1
                ans = max(ans, j - i)

        return ans
