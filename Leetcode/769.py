from typing import List


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        n = len(arr)
        ans = 0
        curr_chunk_sum = req_chunk_sum = 0
        for i in range(n):
            req_chunk_sum += i
            curr_chunk_sum += arr[i]
            if req_chunk_sum == curr_chunk_sum:
                ans += 1
                req_chunk_sum = curr_chunk_sum = 0
        return ans
