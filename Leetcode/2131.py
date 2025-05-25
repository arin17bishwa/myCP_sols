from collections import Counter
from typing import List


class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        ans = 0
        single_exists: bool = False
        freq = Counter(words)

        for word, cnt in freq.items():
            palindrome = word[::-1]
            if word == palindrome:
                ans += (cnt >> 1) << 2
                if cnt & 1:
                    single_exists = True

            elif word < palindrome and palindrome in freq:
                ans += min(cnt, freq[palindrome]) << 2
        return ans + (single_exists * 2)
