# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
        mn: int = -(10**18)

        def func(node: TreeNode | None) -> tuple[int, int]:
            if not node:
                return mn, mn
            left_straight, left_loop = func(node.left)
            right_straight, right_loop = func(node.right)
            return (
                node.val + max(0, left_straight, right_straight),
                max(
                    left_loop,
                    right_loop,
                    node.val,
                    max(0, left_straight) + max(0, right_straight) + node.val,
                ),
            )

        return max(func(root))
