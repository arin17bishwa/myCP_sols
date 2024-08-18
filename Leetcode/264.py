import heapq


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        primes = [2, 3, 5]
        seen = {1}
        heap = [1]
        mn = 1

        for _ in range(n):
            mn = heapq.heappop(heap)
            for prime in primes:
                x = mn * prime
                if x not in seen:
                    seen.add(x)
                    heapq.heappush(heap, x)

        return mn
