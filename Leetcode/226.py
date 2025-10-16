from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def func(node: TreeNode | None) -> TreeNode | None:
            if not node:
                return
            func(node.left)
            func(node.right)
            node.left, node.right = node.right, node.left

        func(root)
        return root
