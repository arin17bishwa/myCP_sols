from collections import Counter


class Solution:
    def canFormPalindrome(self, s: str) -> bool:
        n = len(s)
        freq = Counter(s)
        odd_frequencies = sum(i & 1 != 0 for i in freq.values())

        if (n & 1 and odd_frequencies == 1) or (n & 1 == 0 and odd_frequencies == 0):
            return True
        return False
