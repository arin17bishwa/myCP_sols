from typing import List


class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        arr = nums
        n = len(arr)
        mx = -1
        ans = 0
        for bitmap in range(1, 1 << n):
            curr = 0
            for i in range(n):
                if bitmap & (1 << i):
                    curr |= arr[i]

            if curr > mx:
                mx = curr
                ans = 1
            elif curr == mx:
                ans += 1
        return ans
