class Solution:
    def maxIndexDifference(self, s: str) -> int:
        n = len(s)
        a_pos = n
        ans = -1
        chars_seen: set[str] = set()

        for idx, ch in enumerate(s):
            if ch == "a":
                if a_pos == n:
                    a_pos = idx
                    ans = 0
                chars_seen.add("a")
            elif chr(ord(ch) - 1) in chars_seen:
                chars_seen.add(ch)
                ans = idx - a_pos

        return ans
