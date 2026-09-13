from typing import List


class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        arr = nums
        expected: set[int] = set(range(min(arr), max(arr) + 1))
        return sorted(expected - set(arr))
