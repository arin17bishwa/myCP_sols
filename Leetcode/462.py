class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        arr = nums
        n = len(arr)
        arr.sort()
        median = arr[n >> 1]
        return sum(abs(median - ele) for ele in arr)
