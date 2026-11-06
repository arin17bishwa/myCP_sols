class Solution:
    def minimumSum(self, s: str) -> int:
        n = len(s)
        i, j = 0, n - 1
        s: list[str] = list(s)

        while i < j:
            a, b = s[i], s[j]
            if a == b:
                pass
            elif a == "?" or b == "?":
                s[i] = s[j] = a if a != "?" else b
            else:
                return -1
            i += 1
            j -= 1

        prev = "?"
        ans: int = 0
        for ch in s:
            if ch != "?":
                if prev != "?":
                    ans += abs(ord(prev) - ord(ch))
                prev=ch

        return ans
