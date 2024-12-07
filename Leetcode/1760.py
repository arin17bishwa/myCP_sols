from math import ceil
from typing import List


class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        arr = nums
        low = 1
        ans = high = 10 ** 9

        while low <= high:
            mid = (low + high) >> 1
            total_ops = sum(map(lambda x: max(0, ceil(x / mid) - 1), arr))
            if total_ops > maxOperations:
                low = mid + 1
            else:
                ans = mid
                high = mid - 1
        return ans
