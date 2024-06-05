import string
from typing import List
from collections import Counter


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        ans = []
        words = [Counter(word) for word in words]
        for ch in string.ascii_lowercase:
            ans.extend([ch] * (min(map(lambda x: x[ch], words))))
        return ans
