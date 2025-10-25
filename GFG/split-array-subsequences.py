import heapq
from collections import Counter


class Solution:
    def isPossible(self, arr: list[int], k: int) -> bool:
        freq: Counter[int] = Counter(arr)

        heap: list[tuple[int, int]] = []
        n = len(arr)
        i = 0
        while i < n:
            curr = arr[i]
            if not heap:
                heapq.heappush(heap, (curr, 1))
                i += 1
            else:
                top = heap[0]
                if curr == top[0]:
                    heapq.heappush(heap, (curr, 1))
                    i += 1
                elif curr == top[0] + 1:
                    heapq.heappop(heap)
                    heapq.heappush(heap, (curr, top[1] + 1))
                    i += 1
                else:
                    if top[1] < k:
                        return False
                    heapq.heappop(heap)

        while heap:
            if heap[0][1] < k:
                return False
            heapq.heappop(heap)
        return True


def main():
    obj = Solution()

    arr = [2, 2, 3, 3, 4, 5]
    k = 2

    # arr = [1, 1, 1, 1, 1]
    # k = 4

    # arr = list(map(int, "8 9 10 11 11 12 13".split()))
    # k = 2

    ans = obj.isPossible(arr, k)

    # print(ans)


if __name__ == "__main__":
    main()
