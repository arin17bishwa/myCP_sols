from typing import List


class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        arr = words

        n = len(arr)
        ans: int = n + 1

        for i in range(startIndex, startIndex + n):
            if arr[i % n] == target:
                ans = min(ans, i - startIndex, n - (i - startIndex))
        return -1 if ans == n + 1 else ans
