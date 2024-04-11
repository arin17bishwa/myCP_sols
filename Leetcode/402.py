from collections import deque


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) == k:
            return "0"
        ans: deque = deque()
        to_pop: int = k
        for digit in num:
            if not ans:
                ans.append(digit)
            else:
                while to_pop > 0 and ans and ans[-1] > digit:
                    ans.pop()
                    to_pop -= 1
                ans.append(digit)
        for _ in range(to_pop):
            ans.pop()
        while ans and ans[0] == "0":
            ans.popleft()

        return "".join(ans) if ans else "0"
