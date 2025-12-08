class Solution:
    def countTriples(self, n: int) -> int:
        ans = 0
        for a in range(1, n + 1):
            for b in range(a, n + 1):
                c2 = a * a + b * b
                c = int(pow(c2, 0.5))
                if c <= n and abs(c * c - c2) < 1e-6:
                    ans += 2
        return ans
