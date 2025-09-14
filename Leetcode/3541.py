from collections import Counter


class Solution:
    def maxFreqSum(self, s: str) -> int:
        freq = Counter(s)
        max_consonant = 0
        for k, v in freq.items():
            if k not in "aeiou":
                max_consonant = max(max_consonant, v)
        return max_consonant + max(freq[i] for i in "aeiou")
