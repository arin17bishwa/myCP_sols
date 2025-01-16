from typing import List


class Solution:
    def subarraySum(self, arr: List[int], target: int):
        start = 0
        curr = 0
        n = len(arr)

        for end, ele in enumerate(arr):
            curr += ele

            while start <= end and curr > target:
                curr -= arr[start]
                start += 1
            if curr == target:
                return [start + 1, end + 1]
        return [-1]
