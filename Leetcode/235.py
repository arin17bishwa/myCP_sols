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
        if None in (root, p, q):
            return root

        mx, mn = max(p.val, q.val), min(p.val, q.val)

        curr = root

        while curr:
            if mn > curr.val:
                curr = curr.right
            elif mx < curr.val:
                curr = curr.left
            else:
                return curr
        return curr
