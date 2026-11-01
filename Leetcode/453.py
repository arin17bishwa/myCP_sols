class Solution:
    def minMoves(self, nums: list[int]) -> int:
        arr = nums
        n = len(arr)
        return sum(arr) - n * min(arr)
