from typing import List


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        return sum(all(ch in allowed for ch in word) for word in words)
