from collections import deque
from typing import Optional, Deque, Tuple


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        split_traversal = traversal.split("-")
        m = len(split_traversal)
        root = TreeNode(int(split_traversal[0]))
        stack: Deque[Tuple[int, TreeNode]] = deque([(0, root)])
        curr_lvl: int = 1
        for idx in range(1, m):
            node_val = split_traversal[idx]
            if node_val == "":
                curr_lvl += 1
                continue
            else:
                new_node = TreeNode(int(node_val))
                while stack and stack[-1][0] != curr_lvl - 1:
                    stack.pop()
                if stack:
                    parent_node: TreeNode = stack[-1][-1]
                    if parent_node.left:
                        parent_node.right = new_node
                    else:
                        parent_node.left = new_node
                stack.append((curr_lvl, new_node))
                curr_lvl = 1
        return root
