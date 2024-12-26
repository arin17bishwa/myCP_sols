from collections import deque
from typing import Dict, Optional, Deque, Tuple


# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


class Solution:
    # Function to return a list of nodes visible from the top view
    # from left to right in Binary Tree.
    def topView(self, root: Optional[Node]):
        view: Dict[int, int] = {0: root.data}
        queue: Deque[Tuple[Node, int]] = deque([(root, 0)])

        while queue:
            curr, pos = queue.popleft()
            if not curr:
                continue
            if pos not in view:
                view[pos] = curr.data

            queue.append((curr.left, pos - 1))
            queue.append((curr.right, pos + 1))

        mn = min(view.keys())
        mx = max(view.keys())
        ans = [0] * (mx - mn + 1)

        for pos, val in view.items():
            ans[pos - mn] = val

        return ans
