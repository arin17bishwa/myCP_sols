from collections import Counter
from typing import List


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, arr: List[int]) -> int:
        for k, v in Counter(arr).items():
            if v > 1:
                return k
        return -1
