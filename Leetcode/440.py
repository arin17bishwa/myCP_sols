class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        k -= 1
        curr = 1

        while k > 0:
            steps = self.count_steps(n, curr)
            if steps <= k:
                k -= steps
                curr += 1
            else:
                curr *= 10
                k -= 1
        return curr

    @staticmethod
    def count_steps(n: int, curr: int):
        steps = 0
        nxt = curr + 1
        while curr <= n:
            steps += min(n + 1, nxt) - curr
            curr *= 10
            nxt *= 10
        return steps
