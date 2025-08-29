from collections import Counter
from typing import List


class Solution:
    def partitionArray(self, nums: List[int], k: int) -> bool:
        arr = nums
        n = len(arr)
        if n % k != 0:
            return False
        req_groups = n // k
        freq = Counter(arr)

        return all(i <= req_groups for i in freq.values())
