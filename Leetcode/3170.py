import heapq


class Solution:
    def clearStars(self, s: str) -> str:
        n = len(s)
        heap = []
        for idx, ch in enumerate(s):
            if ch != "*":
                heapq.heappush(heap, (ch, -idx))
            else:
                _ = heapq.heappop(heap)

        ans: list[str] = [""] * n
        for ch, neg_idx in heap:
            ans[-neg_idx] = ch
        return "".join(ans)
