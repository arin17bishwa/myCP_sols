import string


class Solution:
    def smallestWindow(self, s: str, p: str) -> str:
        def is_valid():
            nonlocal window_counter, required_counter
            for k, v in required_counter.items():
                if window_counter[k] < v:
                    return False
            return True

        ans = [-1, -1]
        window_counter: dict[str, int] = {ch: 0 for ch in string.ascii_lowercase}
        required_counter = window_counter.copy()
        for ch in p:
            required_counter[ch] += 1

        tail = 0
        n = len(s)
        for head in range(n):
            window_counter[s[head]] += 1
            while is_valid():
                if ans[0] == -1 or head - tail < ans[1] - ans[0]:
                    ans = [tail, head]
                window_counter[s[tail]] -= 1
                tail += 1
        return "" if ans[0] == -1 else s[ans[0] : ans[1] + 1]
