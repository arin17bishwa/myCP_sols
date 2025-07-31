from typing import List
from collections import defaultdict


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        arr = nums
        freq = defaultdict(int)
        n = len(arr)
        current_sum = ans = tail = 0
        for head in range(n):
            x = arr[head]
            while freq[x]:
                current_sum -= arr[tail]
                freq[arr[tail]] -= 1
                tail += 1
            freq[x] += 1
            current_sum += x
            ans = max(ans, current_sum)
        return ans
