from typing import List


class Solution:
    def check(self, nums: List[int]) -> bool:
        arr = nums
        n = len(arr)
        rotations: List[int] = []
        first = None
        for i in range(1, n):
            if first is None:
                first = i
            if arr[i - 1] > arr[i]:
                if rotations:
                    return False
                rotations = [first, arr[i - 1]]
                if not arr[0] >= arr[-1]:
                    return False
        return True
