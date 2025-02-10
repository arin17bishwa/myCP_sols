from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        arr = prices
        mn = arr[0]
        ans = 0
        for i in arr:
            ans = max(ans, i - mn)
            mn = min(mn, i)
        return ans
