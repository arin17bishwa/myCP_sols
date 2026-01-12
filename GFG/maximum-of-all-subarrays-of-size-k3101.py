import heapq


class Solution:
    def maxOfSubarrays(self, arr: list[int], k: int) -> list[int]:
        n = len(arr)
        heap: list[tuple[int, int]] = [(-arr[i], i) for i in range(k)]
        heapq.heapify(heap)
        ans: list[int] = []

        for i in range(k, n):
            while heap and heap[0][1] < i - k:
                heapq.heappop(heap)
            ans.append(-heap[0][0])
            heapq.heappush(heap, (-arr[i], i))

        while heap and heap[0][1] < n - k:
            heapq.heappop(heap)

        ans.append(-heap[0][0])

        return ans


def main():
    obj = Solution()

    arr = [1, 2, 3, 1, 4, 5, 2, 3, 6]
    k = 3

    arr = [5, 1, 3, 4, 2]
    k = 1

    ans = obj.maxOfSubarrays(arr, k)

    # print(ans)


if __name__ == "__main__":
    main()
