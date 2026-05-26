class Solution:
    def isAdjacentDiffAtMostTwo(self, s: str) -> bool:
        n = len(s)

        for i in range(1, n):
            if abs(ord(s[i - 1]) - ord(s[i])) > 2:
                return False
        return True
