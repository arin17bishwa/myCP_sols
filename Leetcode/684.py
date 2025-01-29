from typing import List


class DSU:
    def __init__(self, n: int):
        self.n = n
        self.size = [1] * n
        self.parent = list(range(n))

    def find_parent(self, node: int) -> int:
        if node == self.parent[node]:
            return node
        self.parent[node] = self.find_parent(self.parent[node])
        return self.parent[node]

    def union(self, node1: int, node2: int) -> bool:
        parent1, parent2 = self.find_parent(node1), self.find_parent(node2)
        if parent1 == parent2:
            return False
        size1, size2 = self.size[parent1], self.size[parent2]

        if size1 >= size2:
            self.size[parent1] += size2
            self.parent[parent2] = parent1
        else:
            self.size[parent2] += size2
            self.parent[parent1] = parent2

        return True


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dsu = DSU(max(max(edge) for edge in edges) + 1)

        ans = None

        for a, b in edges:
            is_diff_component = dsu.union(a, b)
            if not is_diff_component:
                ans = [a, b]
        return ans
