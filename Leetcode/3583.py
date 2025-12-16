from collections import Counter
from typing import List


class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        mod = 10**9 + 7
        arr = nums
        n = len(arr)
        prefix = Counter()
        suffix = Counter()
        for i in range(n - 1, 0, -1):
            suffix[arr[i]] += 1
        prefix[arr[0]] += 1
        ans = 0
        for j in range(1, n - 1):
            suffix[arr[j]] -= 1
            ans = ans + prefix[arr[j] << 1] * suffix[arr[j] << 1]
            if ans >= mod:
                ans %= mod
            prefix[arr[j]] += 1
        return ans
