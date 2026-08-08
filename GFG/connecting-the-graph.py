class DSU:
    def __init__(self, n: int):
        self.n: int = n
        self.parent: list[int] = list(range(n))
        self.rank: list[int] = [1] * n
        self.components: int = n
        self.extras: int = 0

    def find_final_parent(self, n: int):
        if self.parent[n] != n:
            self.parent[n] = self.find_final_parent(self.parent[n])
        return self.parent[n]

    def add(self, x: int, y: int):
        p1 = self.find_final_parent(x)
        p2 = self.find_final_parent(y)
        if p1 == p2:
            self.extras += 1
        else:
            self.components -= 1

        if self.rank[p1] >= self.rank[p2]:
            self.rank[p1] += self.rank[p2]
            self.parent[p2] = p1
        else:
            self.rank[p2] += self.rank[p1]
            self.parent[p1] = p2

        # print(f"x:{x},y:{y},p1:{p1},p2:{p2}")
        # print(self.parent)

    def is_sibling(self, x: int, y: int) -> bool:
        return self.parent[x] == self.parent[y]


class Solution:
    def minEdgesReq(self, n: int, edges: list[list[int]]) -> int:
        dsu = DSU(n)

        for u, v in edges:
            dsu.add(u, v)

        # print(list(range(n)))
        # print(dsu.parent)
        # print(dsu.rank)
        # print(dsu.components)
        # print(dsu.extras)

        if dsu.extras < dsu.components - 1:
            return -1
        return dsu.components - 1


def main():
    obj = Solution()

    n = 4
    arr = [[0, 1], [0, 2], [1, 2]]

    # n=6
    # arr=[[0, 1], [0, 3], [1, 3], [4,5]]

    # n=6
    # arr=[[0,1], [0,2], [0,3], [1,2], [1,3]]

    # n=10
    # arr=[[2, 7], [6, 1], [4, 2], [3, 2], [2, 1], [6, 8]]

    n = 9
    arr = [
        [0, 2],
        [0, 3],
        [1, 4],
        [1, 7],
        [2, 7],
        [3, 6],
        [4, 5],
        [4, 8],
        [5, 7],
        [6, 7],
        [6, 8],
    ]

    ans = obj.minEdgesReq(n, arr)

    # print(ans)


if __name__ == "__main__":
    main()
