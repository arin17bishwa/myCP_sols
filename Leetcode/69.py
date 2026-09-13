class Solution:
    def mySqrt(self, x: int) -> int:
        lo, hi = 0, x + 1
        ans = hi
        e = 1e-6
        while (hi - lo) >= e:
            mid = (lo + hi) / 2
            k = mid * mid
            if (k - x) >= e:
                hi = mid
                ans = mid
            else:
                lo = mid
        return int(ans)
