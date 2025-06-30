from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        arr = prices
        ans = 0
        mn = arr[0]
        for i in arr:
            if i <= mn:
                mn = i
            else:
                ans = max(ans, i - mn)
        return ans
