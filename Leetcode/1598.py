from typing import List
from collections import deque


class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = deque()
        for log in logs:
            if log == "../":
                if stack:
                    stack.pop()
            elif log != "./":
                stack.append(log)
        return len(stack)
