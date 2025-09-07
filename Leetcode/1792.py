import heapq
from typing import List


class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:

        def calculate_gain(p: int, t: int) -> float:
            return ((p + 1) / (t + 1)) - (p / t)

        arr = classes
        arr = [[-calculate_gain(*i)] + i for i in arr]
        heapq.heapify(arr)

        while extraStudents:
            _, pass_, total = heapq.heappop(arr)
            heapq.heappush(
                arr, [-calculate_gain(pass_ + 1, total + 1), pass_ + 1, total + 1]
            )
            extraStudents -= 1

        return sum(i[1] / i[2] for i in arr) / len(arr)
