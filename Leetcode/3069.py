from typing import List


class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        arr1: list[int] = [nums[0]]
        arr2: list[int] = [nums[1]]

        for i in range(2, n):
            if arr1[-1] > arr2[-1]:
                arr1.append(nums[i])
            else:
                arr2.append(nums[i])

        return arr1 + arr2
