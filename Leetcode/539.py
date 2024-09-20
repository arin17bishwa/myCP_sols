from typing import List


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def to_mins(s: str) -> int:
            h, m = map(int, s.split(":"))
            return 60 * h + m

        times = sorted(map(to_mins, timePoints))
        n = len(times)
        ans = float("inf")
        for i in range(1, n):
            ans = min(times[i] - times[i - 1], ans)
        return min(ans, 1440 + times[0] - times[-1])
