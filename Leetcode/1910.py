from collections import deque
from typing import Deque, List


class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack: List[str] = []
        curr: Deque[str] = deque()
        n, m = len(s), len(part)
        part_list = deque(part)

        for ch in s:
            stack.append(ch)
            curr.append(ch)
            # print(1, stack)
            # print(2, curr)
            if len(curr) > m:
                curr.popleft()
            if ch == part[-1] and part_list == curr:
                for _ in range(m):
                    stack.pop()
                curr = deque(stack[-m:])
        return "".join(stack)


def main():
    obj = Solution()
    s = "daabcbaabcbc"
    t = "abc"
    ans = obj.removeOccurrences(s, t)
    print(ans)


if __name__ == "__main__":
    main()
