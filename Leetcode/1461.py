class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        n = len(s)
        if n < k:
            return False
        curr = 0
        for i in range(k):
            curr = (curr << 1) | (1 if s[i] == "1" else 0)
        seen = {curr}
        mask = (1 << k) - 1
        for i in range(k, n):
            curr = (curr << 1) | (1 if s[i] == "1" else 0)
            curr &= mask
            seen.add(curr)
        return len(seen) == (1 << k)
