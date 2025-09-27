from collections import deque


class Solution:
    def rotateDeque(self, dq: deque, tp: int, k: int) -> None:
        n = len(dq)
        k %= n
        while k:
            if tp == 1:
                dq.appendleft(dq.pop())
            else:
                dq.append(dq.popleft())
            k -= 1
