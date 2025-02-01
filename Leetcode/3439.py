from typing import List


class Solution:
    def maxFreeTime(
        self, eventTime: int, k: int, startTime: List[int], endTime: List[int]
    ) -> int:
        n = len(startTime)
        meetings = sorted(zip(startTime, endTime))
        starts_times, end_times = zip(*meetings)
        starts_times = list(starts_times)
        end_times = list(end_times)
        if starts_times[0]:
            gaps = [starts_times[0]]
        else:
            gaps = []
        for i in range(n - 1):
            gaps.append(starts_times[i + 1] - end_times[i])
        if end_times[-1] < eventTime:
            gaps.append(eventTime - end_times[-1])

        m = len(gaps)
        if len(gaps) <= k:
            return sum(gaps)

        curr = 0
        k += 1
        for i in range(k):
            curr += gaps[i]
        ans = curr
        for i in range(k, m):
            curr += gaps[i] - gaps[i - k]
            ans = max(ans, curr)
        return ans
