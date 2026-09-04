class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        arr = nums
        n = len(arr)
        mn = arr[:]
        mx = arr[0]
        for i in range(n - 2, -1, -1):
            mn[i] = min(mn[i], mn[i + 1])

        for i in range(n):
            mx = max(mx, arr[i])
            if mx - mn[i] <= k:
                return i

        return -1
