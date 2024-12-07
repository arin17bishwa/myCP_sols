from math import ceil
from typing import List


class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        arr = nums
        low = 1
        ans = high = max(arr)

        while low <= high:
            mid = (low + high) >> 1
            total_ops = sum(map(lambda x: self.get_number_of_ops(x, mid), arr))
            if total_ops > maxOperations:
                low = mid + 1
            else:
                ans = mid
                high = mid - 1
        return ans

    @staticmethod
    def get_number_of_ops(start: int, target_max: int) -> int:
        if start <= target_max or start <= 1:
            return 0
        return max(0, ceil(start / target_max) - 1)
