from collections import defaultdict, deque
from typing import Optional


class Node:
    def __init__(self, val: int):
        self.data = val
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None


class Solution:
    def verticalOrder(self, root: Optional[Node]) -> list[list[int]]:
        view: defaultdict[int, list[int]] = defaultdict(list)
        q: deque[list[Optional[Node] | int]] = deque([[root, 0]])

        while q:
            node, x = q.popleft()

            if not node:
                continue

            view[x].append(node.data)

            q.append([node.left, x - 1])
            q.append([node.right, x + 1])

        return [view[idx] for idx in sorted(view.keys())]
