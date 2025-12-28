from collections import deque


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_occ: dict[str, int] = {}
        ans: deque[str] = deque()

        for idx, ch in enumerate(s):
            last_occ[ch] = idx

        for idx, ch in enumerate(s):
            if ch not in ans:
                while ans and ans[-1] > ch and last_occ[ans[-1]] > idx:
                    ans.pop()
                ans.append(ch)
        return "".join(ans)
