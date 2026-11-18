class Solution:
    def findPattern(self, s: str) -> bool:
        curr: int = 0

        for idx, ch in enumerate(s):
            if ch == 'x':
                if idx != 0 and (s[idx - 1] != 'x' and curr != 0):
                    return False
                curr += 1
            else:
                curr -= 1
        return curr == 0
