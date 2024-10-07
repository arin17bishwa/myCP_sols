from collections import deque


class Solution:
    def minLength(self, s: str) -> int:
        ans = deque()
        for ch in s:
            if not ans:
                ans.append(ch)
            elif ch == "B" and ans[-1] == "A":
                ans.pop()
            elif ch == "D" and ans[-1] == "C":
                ans.pop()
            else:
                ans.append(ch)
        return len(ans)
