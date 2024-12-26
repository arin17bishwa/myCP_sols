import heapq
from typing import List, Tuple


def mergeKSortedArrays(kArrays: List[List[int]], k: int) -> List[int]:
    # Write your code here.
    # kArrays is a list of 'k' lists.
    # Return a list.
    arr = kArrays

    heap: List[Tuple[int, int]] = []
    for i in range(k):
        heapq.heappush(heap, (arr[i][0], i, 0))
    ans: List[int] = []

    while heap:
        mn, row, col = heapq.heappop(heap)
        ans.append(mn)
        if len(arr[row]) - 1 == col:
            continue
        heapq.heappush(heap, (arr[row][col + 1], row, col + 1))

    return ans
