from typing import List


class Solution:
    def majorityElement(self, arr: List[int]) -> int:
        n = len(arr)
        candidate = arr[0]
        current_freq = 1
        for i in range(1, n):
            if arr[i] == candidate:
                current_freq += 1
            else:
                current_freq -= 1
            if current_freq <= 0:
                candidate = arr[i]
                current_freq = 1
        return candidate
