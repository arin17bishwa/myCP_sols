from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        arr = nums
        n = len(arr)
        lo, mid, hi = 0, 0, n - 1

        while mid <= hi:
            if arr[mid] == 0:
                arr[lo], arr[mid] = arr[mid], arr[lo]
                lo += 1
                mid += 1
            elif arr[mid] == 1:
                mid += 1
            else:
                arr[mid], arr[hi] = arr[hi], arr[mid]
                hi -= 1
