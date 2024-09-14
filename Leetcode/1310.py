from typing import List


class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        arr = [0] + arr
        for i in range(1, len(arr)):
            arr[i] = arr[i] ^ arr[i - 1]
        print(arr)
        return [arr[right + 1] ^ arr[left] for left, right in queries]
