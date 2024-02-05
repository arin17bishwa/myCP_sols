class Solution:
    def balancedStringSplit(self, s: str) -> int:
        cnt = balance = 0

        for ch in s:
            if ch == "L":
                balance -= 1
            else:
                balance += 1
            if balance == 0:
                cnt += 1
        return cnt
