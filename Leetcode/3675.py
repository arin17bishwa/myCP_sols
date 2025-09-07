class Solution:
    def minOperations(self, s: str) -> int:
        return max((26 - (ord(ch) - ord("a"))) % 26 for ch in s)
