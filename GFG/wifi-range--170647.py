class Solution:
    def wifiRange(self, s: str, x: int) -> bool:
        n = len(s)

        if x == 0:
            return s.count("1") == n
        elif x >= n:
            return s.count("1") > 0

        arr = [0] * (n + 1)

        for idx, ch in enumerate(s):
            if ch == "1":
                arr[max(0, idx - x)] += 1
                arr[min(n, idx + x + 1)] -= 1

        for i in range(1, n + 1):
            arr[i] += arr[i - 1]

        return all(arr[i] > 0 for i in range(n))
