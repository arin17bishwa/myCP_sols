from collections import deque
from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        arr = nums
        n = len(arr)
        converted = deque()
        ans = tail = 0

        for head in range(n):
            ele = arr[head]
            if ele == 0:
                if k>0:
                    while converted and len(converted) == k:
                        if converted[0] == tail:
                            _ = converted.popleft()
                        tail += 1
                    converted.append(head)
                else:
                    tail=head+1

            ans = max(ans, head - tail + 1)
        return ans
