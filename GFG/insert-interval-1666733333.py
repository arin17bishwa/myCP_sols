class Solution:
    def insertInterval(
        self, intervals: list[list[int]], newInterval: list[int]
    ) -> list[list[int]]:
        intervals.append(newInterval)
        intervals.sort()
        ans: list[list[int]] = []

        curr = intervals[0]
        for start, end in intervals:
            if start <= curr[1]:
                curr[1] = max(curr[1], end)
            else:
                ans.append(curr.copy())
                curr = [start, end]
        if curr:
            ans.append(curr)
        return ans
