from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        arr = nums
        n = len(arr)
        brk = -1
        for i in range(n - 2, -1, -1):
            if arr[i] < arr[i + 1]:
                brk = i
                break
        if brk == -1:
            self.reverse(arr, 0, n - 1)
            return

        for i in range(n - 1, brk, -1):
            if arr[i] > arr[brk]:
                arr[i], arr[brk] = arr[brk], arr[i]
                self.reverse(arr, brk + 1, n - 1)
                return

    @staticmethod
    def reverse(arr: list[int], start: int, end: int):
        for i in range((end - start + 1) >> 1):
            arr[start + i], arr[end - i] = arr[end - i], arr[start + i]
