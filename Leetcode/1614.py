class Solution:
    def maxDepth(self, s: str) -> int:
        ans = curr = 0
        for ch in s:
            if ch == "(":
                curr += 1
            elif ch == ")":
                curr -= 1
            ans = max(ans, curr)
        return ans
