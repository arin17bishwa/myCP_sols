from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        arr = prices
        n = len(arr)
        ans = 0

        for i in range(1, n):
            ans += max(0, arr[i] - arr[i - 1])
            
        return ans
