from collections import Counter
from typing import List


class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        arr = nums
        n = len(arr)
        freq = Counter()
        for i in range(n):
            for j in range(i + 1, n):
                freq[arr[i] * arr[j]] += 1
        return sum((v * (v - 1)) >> 1 for v in freq.values()) << 3
