from collections import Counter
from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        arr = nums
        n = len(arr)
        ans = [0] * 2
        freq = Counter(arr)
        for i in range(1, 1 + n):
            if freq[i] == 2:
                ans[0] = i
            elif freq[i] == 0:
                ans[1] = i
        return ans
