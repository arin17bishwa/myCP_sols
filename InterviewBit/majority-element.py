from collections import Counter
from typing import List


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def majorityElement(self, arr: List[int]) -> int:
        n = len(arr)
        freq = Counter(arr)
        for k, v in freq.items():
            if v > n // 2:
                return k
