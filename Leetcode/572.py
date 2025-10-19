from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if subRoot is None:
            return True
        if root is None:
            return False
        return (
            self.is_same_tree(root, subRoot)
            or self.isSubtree(root.left, subRoot)
            or self.isSubtree(root.right, subRoot)
        )

    def is_same_tree(
        self, node1: Optional[TreeNode], node2: Optional[TreeNode]
    ) -> bool:
        if node1 is None and node2 is None:
            return True
        if node1 is None or node2 is None:
            return False
        return (
            node1.val == node2.val
            and self.is_same_tree(node1.left, node2.left)
            and self.is_same_tree(node1.right, node2.right)
        )
