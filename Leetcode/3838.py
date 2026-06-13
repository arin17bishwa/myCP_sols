from typing import List


class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        def transform(s: str) -> int: ...

        ans = []

        for word in words:
            total_weight = sum(weights[ord(ch)-97] for ch in word)
            ans.append(chr(ord("z") - (total_weight % 26)))

        return "".join(ans)
