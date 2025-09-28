from typing import List


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        arr = nums
        arr.sort(reverse=True)
        n = len(arr)
        for i in range(n - 2):
            if arr[i + 2] + arr[i + 1] > arr[i]:
                return sum(arr[i : i + 3])
        return 0
