import heapq
from collections import Counter
from typing import List, Tuple


class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        heap: List[Tuple[int, int]] = list(Counter(map(lambda x: -ord(x), s)).items())
        heapq.heapify(heap)
        ans: List[str] = []
        holder: List[Tuple[int, int]] = []
        while heap:
            neg_ascii, freq = heapq.heappop(heap)
            ch: str = chr(-neg_ascii)
            if (not holder) or (holder[0][0] > neg_ascii):
                rep = min(repeatLimit, freq)
            else:
                rep = 1
            ans.append(ch * rep)
            if holder:
                heapq.heappush(heap, holder.pop())
            if rep < freq:
                holder.append((-ord(ch), freq - rep))

        return "".join(ans)
