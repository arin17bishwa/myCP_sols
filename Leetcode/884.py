from typing import List
from collections import Counter


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        return [
            word for word, freq in Counter((s1 + " " + s2).split()).items() if freq == 1
        ]
