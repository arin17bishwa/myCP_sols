# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        if not p or not q:
            return root

        def func(node: TreeNode | None):
            nonlocal p, q
            if not node:
                return None
            if max(p.val, q.val) < node.val:
                return func(node.left)
            if min(p.val, q.val) > node.val:
                return func(node.right)
            return node

        return func(node=root)
