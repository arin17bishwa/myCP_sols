from collections import Counter
from typing import List


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def majorityElement(self, A: List[int]) -> int:
        arr = A
        n = len(arr)
        freq = Counter(arr)
        for k, v in freq.items():
            if v > n // 2:
                return k
        return -1
