from typing import List


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        arr = [int(i, 2) for i in nums]
        arr.sort()
        n = len(arr)
        for i in range(n):
            if i != arr[i]:
                return bin(i)[2:].zfill(n)
        return bin(n)[2:].zfill(n)
