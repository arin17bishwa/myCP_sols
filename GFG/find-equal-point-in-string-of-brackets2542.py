class Solution:
    def findIndex(self, s: str) -> int:
        n = len(s)
        closing = s.count(")")
        opening = 0

        if closing == n:
            return n
        elif closing == 0:
            return 0

        for idx, ch in enumerate(s):
            if ch == ")":
                closing -= 1
            else:
                opening += 1
            if closing == opening:
                return idx + 1

        return -1
