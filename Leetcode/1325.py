# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def removeLeafNodes(self, root: TreeNode | None, target: int) -> TreeNode | None:

        def func(node: TreeNode | None) -> TreeNode | None:
            nonlocal target

            if not node:
                return None

            node.left = func(node.left)
            node.right = func(node.right)

            if node.left is None and node.right is None and node.val == target:
                return None

            return node

        return func(root)
