from collections import deque


class Solution:
    def clearDigits(self, s: str) -> str:
        stack = deque()
        for ch in s:
            if ch.isdigit():
                stack.pop()
            else:
                stack.append(ch)
        return "".join(stack)
