from typing import List


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def majorityElement(self, A: List[int]) -> int:
        arr = A
        n = len(arr)
        candidate = arr[0]
        curr_freq = 0
        for i in range(n):
            if arr[i] == candidate:
                curr_freq += 1
            else:
                curr_freq -= 1
                if curr_freq < 0:
                    candidate = arr[i]
                    curr_freq = 1
        return candidate
