from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        arr = height
        n = len(arr)
        i, j = 0, n - 1
        ans = 0
        while i < j:
            ans = max(ans, min(arr[i], arr[j]) * (j - i))
            if arr[i] <= arr[j]:
                i += 1
            else:
                j -= 1
        return ans
