from typing import List


class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        arr = happiness
        arr.sort(reverse=True)
        if arr[k - 1] >= k:
            return sum(arr[:k]) - (k * (k - 1)) // 2
        ans = 0
        for i in range(k):
            ans += max(0, arr[i] - i)
        return ans
