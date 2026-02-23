class Solution:
    def findMinDiff(self, arr: list[int], m: int):
        arr.sort()
        n = len(arr)
        ans = arr[-1] - arr[0]
        for i in range(m - 1, n):
            ans = min(ans, arr[i] - arr[i - m + 1])
        return ans
