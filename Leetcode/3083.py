class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        n = len(s)
        seen: set[str] = set((s[i : i + 2][::-1] for i in range(n - 1)))
        for i in range(n - 1):
            if s[i : i + 2] in seen:
                return True
        return False
