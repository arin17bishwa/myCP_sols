from collections import Counter


class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        s1_even = Counter(s1[::2])
        s1_odd = Counter(s1[1::2])
        s2_even = Counter(s2[::2])
        s2_odd = Counter(s2[1::2])

        return s1_even == s2_even and s1_odd == s2_odd
