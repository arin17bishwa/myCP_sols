from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        arr = citations
        n = len(arr)
        lo, hi = 0, n
        ans = 0
        while lo <= hi:
            mid = (lo + hi) >> 1
            if sum(citation_count >= mid for citation_count in citations) >= mid:
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1
        return ans
