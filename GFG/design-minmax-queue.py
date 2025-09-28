import heapq
from collections import deque


class SpecialQueue:
    def __init__(self):
        self.dq = deque()
        self.lower_bound = 0
        self.upper_bound = 0
        self.min_heap = []
        self.max_heap = []

    def _insertion_bookkeeping(self):
        self.upper_bound += 1

    def _deletion_bookkeeping(self):
        self.lower_bound += 1

    def enqueue(self, x):
        heapq.heappush(self.min_heap, (x, self.upper_bound))
        heapq.heappush(self.max_heap, (-x, self.upper_bound))

        self.dq.append(x)

        self._insertion_bookkeeping()

    def dequeue(self):
        self.dq.popleft()

        self._deletion_bookkeeping()

    def getFront(self):
        return self.dq[0]

    def getMin(self):
        while self.min_heap and not (
            self.lower_bound <= self.min_heap[0][1] <= self.upper_bound
        ):
            heapq.heappop(self.min_heap)
        return self.min_heap[0][0]

    def getMax(self):
        while self.max_heap and not (
            self.lower_bound <= self.max_heap[0][1] <= self.upper_bound
        ):
            heapq.heappop(self.max_heap)
        return -self.max_heap[0][0]
