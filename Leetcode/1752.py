from typing import List


class Solution:
    def check(self, nums: List[int]) -> bool:
        arr = nums
        n = len(arr)
        rotations = 0

        for i in range(1, n):
            if arr[i - 1] > arr[i]:
                rotations += 1

        if arr[0] < arr[-1]:
            rotations += 1
        return rotations <= 1
