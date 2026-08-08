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


class Solution:
    def minEdgesReq(self, n: int, edges: list[list[int]]) -> int:
        dsu = DSU(n)

        for u, v in edges:
            dsu.add(u, v)

        if dsu.extras < dsu.components - 1:
            return -1
        return dsu.components - 1
