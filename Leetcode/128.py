from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        arr = nums
        seen: set[int] = set(arr)

        ans = 0
        for i in seen:
            if i - 1 in seen:
                continue
            j = i + 1
            curr = 1
            while j in seen:
                curr += 1
                j += 1
            ans = max(ans, curr)
        return ans
