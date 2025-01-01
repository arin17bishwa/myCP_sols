from typing import List


class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        total_zeroes = s.count("0")
        left_zeroes = ans = 0
        for idx in range(n - 1):
            if s[idx] == "0":
                left_zeroes += 1
            ans = max(ans, left_zeroes + (n - idx - 1 - (total_zeroes - left_zeroes)))

        return ans
