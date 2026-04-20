class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        arr = nums
        n = len(arr)
        prefix = arr[:]
        suffix = arr[:]

        for i in range(1, n):
            prefix[i] = max(prefix[i], prefix[i - 1])

        for i in range(n - 2, -1, -1):
            suffix[i] = min(suffix[i], suffix[i + 1])

        for i in range(n):
            if prefix[i] - suffix[i] <= k:
                return i
        return -1
