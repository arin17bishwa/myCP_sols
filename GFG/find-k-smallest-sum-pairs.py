import heapq


class Solution:
    def kSmallestPair(
        self, arr1: list[int], arr2: list[int], k: int
    ) -> list[list[int]]:
        heap: list[tuple[int, int, int]] = [(arr1[0] + arr2[0], 0, 0)]
        m, n = len(arr1), len(arr2)
        ans: list[list[int]] = []
        vis: set[tuple[int, int]] = set()
        while len(ans) < k and heap:
            print(heap[0])
            _, top_i, top_j = heapq.heappop(heap)

            ans.append([arr1[top_i], arr2[top_j]])
            if top_i + 1 < m and (top_i + 1, top_j) not in vis:
                heapq.heappush(heap, (arr1[top_i + 1] + arr2[top_j], top_i + 1, top_j))
                vis.add((top_i + 1, top_j))
            if top_j + 1 < n and (top_i, top_j + 1) not in vis:
                heapq.heappush(heap, (arr1[top_i] + arr2[top_j + 1], top_i, top_j + 1))
                vis.add((top_i, top_j + 1))

        return ans


def main():
    obj = Solution()

    arr1 = [6, 6, 9, 10, 10, 11, 12]
    arr2 = [4, 5, 5, 6, 10, 11, 13]
    k = 10

    arr1=[2,8,9,12]
    arr2=[2,8,9,12]
    k=26
    temp=[]
    for i in arr1:
        for j in arr2:
            temp.append([i,j])

    ans = obj.kSmallestPair(arr1, arr2, k)

    print(ans)

    print(sorted(temp, key=lambda x: sum(x))[:k])


if __name__ == "__main__":
    main()
