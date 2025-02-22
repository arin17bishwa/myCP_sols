from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        arr = nums
        n = len(arr)
        min_jumps = [float("inf")] * n
        min_jumps[0] = 0
        for i in range(n):
            for j in range(i + 1, min(n, i + arr[i] + 1)):
                min_jumps[j] = min(min_jumps[j], min_jumps[i] + 1)
        return int(min_jumps[-1])
