from typing import List


class Solution:
    def check(self, nums: List[int]) -> bool:
        arr = nums
        n = len(arr)
        rotations: int = 0
        for i in range(1, n):
            if arr[i - 1] > arr[i]:
                if rotations:
                    return False
                rotations += 1
                if not arr[0] >= arr[-1]:
                    return False
        return True
