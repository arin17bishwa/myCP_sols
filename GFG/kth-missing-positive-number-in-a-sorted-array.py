class Solution:
    def kthMissing(self, arr: list[int], k: int) -> int:
        n = len(arr)
        lo, hi = 0, n - 1
        ans = -1

        while lo <= hi:
            mid = (lo + hi) >> 1
            if arr[mid] > mid + k:
                ans = mid + k
                hi = mid - 1
            else:
                lo = mid + 1

        return n + k if ans == -1 else ans
