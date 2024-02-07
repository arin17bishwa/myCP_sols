from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)
        return "".join(
            (
                k * v
                for k, v in sorted(Counter(s).items(), key=lambda x: x[1], reverse=True)
            )
        )
