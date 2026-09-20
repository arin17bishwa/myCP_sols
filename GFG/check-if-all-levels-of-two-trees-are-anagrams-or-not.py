from collections import deque, Counter


class Node:
    def __init__(self, x: int):
        self.data = x
        self.left = self.right = None


class Solution:
    def areAnagrams(self, root1: Node | None, root2: Node | None):
        return self.level_wise_freq(root1) == self.level_wise_freq(root2)

    @staticmethod
    def level_wise_freq(node: Node | None) -> list[Counter[int]]:
        if not node:
            return []
        res: list[Counter[int]] = []
        q = deque([node])

        while q:
            lvl = Counter()
            for _ in range(len(q)):
                curr = q.popleft()
                lvl[curr.data] += 1

                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)

            res.append(lvl.copy())
        return res

        return res
