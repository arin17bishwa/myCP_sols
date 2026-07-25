class Solution:
    def maxPeopleDefeated(self, p: int) -> int:
        def sum_of_squares(n: int) -> int:
            return ((n * (n + 1) * ((n << 1) | 1)) // 3) >> 1

        lo, hi = 0, 10**3
        ans = lo
        while lo <= hi:
            mid = (lo + hi) >> 1
            if sum_of_squares(mid) <= p:
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1
        return ans
