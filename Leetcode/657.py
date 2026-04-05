from collections import Counter


class Solution:
    def judgeCircle(self, moves: str) -> bool:
        freq = Counter(moves)
        return freq["U"] == freq["D"] and freq["L"] == freq["R"]
