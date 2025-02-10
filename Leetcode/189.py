from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        arr = nums
        n = len(arr)
        k %= n
        if k == 0:
            return
        arr[:] = arr[-k:] + arr[: n - k]
