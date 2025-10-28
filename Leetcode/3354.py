from typing import List


class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        arr = nums
        n = len(arr)

        if n == 1:
            return int(arr[0] == 0) * 2

        prefix = arr[:]
        suffix = arr[:]

        for i in range(1, n):
            prefix[i] += prefix[i - 1]

        for i in range(n - 2, -1, -1):
            suffix[i] += suffix[i + 1]

        ans: int = 0
        if arr[0] == 0 and suffix[0] <= 1:
            ans += 1 if suffix[0] == 1 else 2
        if arr[-1] == 0 and prefix[-1] <= 1:
            ans += 1 if prefix[-1] == 1 else 2

        for i in range(1, n - 1):
            if arr[i] == 0:
                if abs(prefix[i - 1] - suffix[i + 1]) == 1:
                    ans += 1
                elif abs(prefix[i - 1] - suffix[i + 1]) == 0:
                    ans += 2

        return ans
