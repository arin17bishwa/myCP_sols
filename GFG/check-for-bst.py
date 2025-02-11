from typing import Optional, Tuple, Union


class Node:
    def __init__(self, val: int):
        self.data = val
        self.left = None
        self.right = None


class Solution:

    def isBST(self, root: Optional[Node]) -> bool:

        def dfs(
            node: Optional[Node],
        ) -> Tuple[bool, Union[int, float], Union[int, float]]:
            if not node:
                return True, float("inf"), float("-inf")
            is_left_bst, left_min, left_max = dfs(node.left)
            is_right_bst, right_min, right_max = dfs(node.right)
            if (not all([is_right_bst, is_left_bst])) or (
                not (left_max <= node.data <= right_min)
            ):
                return False, 0, 0
            return True, min(left_min, node.data), max(right_max, node.data)

        return dfs(root)[0]
