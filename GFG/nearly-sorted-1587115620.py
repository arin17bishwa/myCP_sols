import heapq


class Solution:
    def nearlySorted(self, arr: list[int], k: int) -> None:
        n = len(arr)
        heap = arr[: k + 1]
        heapq.heapify(heap)
        i = k + 1
        for idx in range(n):
            if i < n:
                heapq.heappush(heap, arr[i])
                i += 1

            arr[idx] = heapq.heappop(heap)
        return


def main():
    obj = Solution()

    arr = [2, 3, 1, 4]
    k = 2

    arr = [7, 9, 14]
    k = 1
    obj.nearlySorted(arr, k)

    # print(arr)


if __name__ == "__main__":
    main()
