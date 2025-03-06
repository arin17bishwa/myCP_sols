from collections import Counter
from typing import List


class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        freq = Counter()
        for row in grid:
            for i in row:
                freq[i] += 1
        ans = [0, 0]

        for i in range(1, len(freq) + 2):
            if freq[i] == 0:
                ans[1] = i
            elif freq[i] == 2:
                ans[0] = i
        return ans
