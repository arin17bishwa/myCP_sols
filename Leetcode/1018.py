from typing import List


class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        arr = nums
        n = len(arr)
        ans = [False] * n
        curr = 0
        for i in range(n):
            curr = (curr << 1) | arr[i]
            if curr % 5 == 0:
                ans[i] = True
        return ans
