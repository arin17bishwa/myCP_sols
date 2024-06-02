from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        for i in range(n >> 1):
            s[i], s[n - i - 1] = s[n - i - 1], s[i]
