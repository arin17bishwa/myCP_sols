from collections import defaultdict, deque


class kQueues:

    def __init__(self, n: int, k: int):
        self.queues = defaultdict(deque)
        self.n = n
        self.k = k
        self.curr_size = 0

    def enqueue(self, x: int, i: int) -> None:
        self.queues[i].append(x)
        self.curr_size += 1

    def dequeue(self, i: int) -> int:
        if self.isEmpty(i):
            return -1
        self.curr_size -= 1
        return self.queues[i].popleft()

    def isEmpty(self, i):
        return len(self.queues[i]) == 0

    def isFull(self):
        return self.curr_size == self.n
