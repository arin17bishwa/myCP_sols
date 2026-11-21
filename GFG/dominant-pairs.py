from bisect import bisect_left


class Solution:
    def dominantPairs(self, arr: list[int]) -> int:
        m = len(arr) >> 1

        first_half = sorted(arr[:m])
        ans = 0

        for i in range(m, len(arr)):
            x = bisect_left(first_half, 5 * arr[i])
            ans += m - x

        return ans
