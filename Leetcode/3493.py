from typing import List


class DSU:
    def __init__(self, n: int):
        self.n = n
        self.parent = [i for i in range(n)]
        self.rank = [1] * n

    def find_parent(self, x: int) -> int:
        while x != self.parent[x]:
            x = self.parent[x]
        return x

    def union(self, x: int, y: int):
        p1, p2 = self.find_parent(x), self.find_parent(y)
        if self.rank[p1] < self.rank[p2]:
            self.parent[p1] = p2
            self.rank[p1] += self.rank[p2]
        else:
            self.parent[p2] = p1
            self.rank[p2] += self.rank[p1]

        return


class Solution:
    def numberOfComponents(self, properties: List[List[int]], k: int) -> int:
        arr: list[set[int]] = [set(i) for i in properties]
        n, m = len(properties), len(properties[0])
        dsu = DSU(n)

        for i in range(n - 1):
            for j in range(i + 1, n):
                if len(arr[i].intersection(arr[j])) >= k:
                    dsu.union(i, j)
        return sum(dsu.find_parent(i) == i for i in range(n))


def main():
    obj = Solution()

    arr = [[1, 2], [1, 1], [3, 4], [4, 5], [5, 6], [7, 7]]
    k = 1

    arr = [[1, 2, 3], [2, 3, 4], [4, 3, 5]]
    k = 2

    arr = [[1, 1], [1, 1]]
    k = 2

    ans = obj.numberOfComponents(arr, k)

    print(ans)


if __name__ == "__main__":
    main()
