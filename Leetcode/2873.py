from typing import List


class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        arr = nums
        n = len(arr)
        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    ans = max(ans, (arr[i] - arr[j]) * arr[k])
        return ans
