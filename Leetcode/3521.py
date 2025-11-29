from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        arr = nums
        sm = sum(arr)
        return sm % k
