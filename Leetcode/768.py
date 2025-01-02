from typing import List


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        n = len(arr)
        target = sorted(arr)
        ans = 0
        curr_chunk_sum = req_chunk_sum = 0

        for i in range(n):
            req_chunk_sum += target[i]
            curr_chunk_sum += arr[i]
            if curr_chunk_sum == req_chunk_sum:
                ans += 1
                curr_chunk_sum = req_chunk_sum = 0
        return ans
