from typing import List


class Solution:
    def triangleType(self, nums: List[int]) -> str:
        arr = nums
        arr.sort()
        if arr[0] + arr[1] <= arr[2]:
            return "none"
        if arr[0] == arr[1] == arr[2]:
            return "equilateral"
        if arr[0] == arr[1] or arr[1] == arr[2]:
            return "isosceles"
        return "scalene"
