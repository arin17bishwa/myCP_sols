class Solution:
    def minMoves(self, nums: list[int]) -> int:
        arr = nums
        n = len(arr)
        mn = 10**10
        sm = 0
        for i in arr:
            sm += i
            mn = min(mn, i)

        return sm - mn * n
