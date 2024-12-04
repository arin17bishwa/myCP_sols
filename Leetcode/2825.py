class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        m, n = len(str1), len(str2)
        i = j = 0
        while i < m and j < n:
            if self.is_doable(str1[i], str2[j]):
                j += 1
            i += 1
        return j == n

    @staticmethod
    def is_doable(a: str, b: str) -> bool:
        if a == b:
            return True
        x, y = ord(a), ord(b)
        if y - x == 1:
            return True
        if a == "z" and b == "a":
            return True
        return False
