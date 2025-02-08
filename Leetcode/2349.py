import heapq
from collections import defaultdict
from typing import List, Dict


class NumberContainers:

    def __init__(self):
        self.index_mappings: defaultdict[int, List[int]] = defaultdict(list)
        self.container_mapping: Dict[int, int] = {}

    def change(self, index: int, number: int) -> None:
        self.container_mapping[index] = number
        heapq.heappush(self.index_mappings[number], index)

    def find(self, number: int) -> int:
        while self.index_mappings[number]:
            lowest_idx = self.index_mappings[number][0]
            if self.container_mapping[lowest_idx] == number:
                return lowest_idx
            else:
                _ = heapq.heappop(self.index_mappings[number])
        return -1
