from collections import Counter
from typing import List


class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        arr = nums
        n = len(arr)
        for i in range(n):
            arr[i] -= i
        return ((n * (n - 1)) // 2) - sum(
            map(lambda x: (x * (x - 1)) // 2, Counter(arr).values())
        )
