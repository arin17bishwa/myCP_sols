import heapq


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        arr = nums
        heapq.heapify(arr)
        return heapq.nlargest(k, arr)[-1]
