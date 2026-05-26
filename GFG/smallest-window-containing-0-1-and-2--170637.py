class Solution:
    def smallestSubstring(self, s: str) -> int:
        freq: dict[str, int] = {"0": 0, "1": 0, "2": 0}
        n = len(s)
        ans = 10**9

        def is_valid():
            return all(freq.values())

        tail = 0

        for head in range(n):
            freq[s[head]] += 1

            while head - tail >= 2 and is_valid():
                ans = min(ans, head - tail + 1)
                freq[s[tail]] -= 1
                tail += 1

        return -1 if ans == 10**9 else ans
