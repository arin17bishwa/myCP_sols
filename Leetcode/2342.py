from collections import defaultdict
from typing import List


class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        arr = nums
        n = len(arr)
        freq = defaultdict(list)
        for i in arr:
            freq[sum(map(int, str(i)))].append(i)
        for v in freq.values():
            v.sort()
        ans = -1
        for v in freq.values():
            if len(v) > 1:
                ans = max(ans, v[-2] + v[-1])
        return ans
