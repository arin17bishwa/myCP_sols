from collections import defaultdict
from typing import List


class Solution:
    def centeredSubarrays(self, nums: List[int]) -> int:
        arr = nums
        n = len(arr)
        ans = 0

        for l in range(n):
            curr_sum = 0
            freq = defaultdict(int)

            for r in range(l, n):
                curr_sum += arr[r]
                freq[arr[r]] += 1

                ans += freq[curr_sum] != 0

        return ans
