from typing import List


class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        arr = nums
        n = len(arr)
        ans = 10**18
        for size in range(l, r + 1):
            curr = 0
            for i in range(n):
                curr += arr[i]
                if i >= size:
                    curr -= arr[i - size]
                if i >= size - 1 and curr > 0:
                    ans = min(ans, curr)

        return -1 if ans == 10**18 else ans
