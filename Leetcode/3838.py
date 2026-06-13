from typing import List


class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:

        ans = [
            chr(ord("z") - (sum(weights[ord(ch) - ord("a")] for ch in word) % 26))
            for word in words
        ]

        return "".join(ans)
