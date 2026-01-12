class Solution:
    def residuePrefixes(self, s: str) -> int:
        n = len(s)
        ans = 0
        seen = set()
        for i in range(n):
            seen.add(s[i])
            if (i + 1) % 3 == len(seen):
                ans += 1
        return ans
