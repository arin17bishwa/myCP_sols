class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        arr = nums
        n = len(arr)
        mx = arr[0]
        suffix = arr[:]

        for i in range(n - 2, -1, -1):
            suffix[i] = min(suffix[i], suffix[i + 1])

        for i in range(n):
            mx = max(mx, arr[i])
            if mx - suffix[i] <= k:
                return i
        return -1
