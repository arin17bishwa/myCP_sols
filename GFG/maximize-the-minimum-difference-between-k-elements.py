class Solution:
    def maxMinDiff(self, arr: list[int], k: int) -> int:
        arr = sorted(set(arr))
        n = len(arr)

        def check(x: int) -> bool:
            nonlocal arr, k
            cnt = 0
            last = -1000000000
            for i in arr:
                if i - last >= x:
                    cnt += 1
                    last = i
            return cnt >= k

        if n < k:
            return 0
        lo, hi = 0, arr[-1] - arr[0]
        ans = 0
        while lo <= hi:
            mid = (lo + hi) >> 1
            if check(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1
        return ans
