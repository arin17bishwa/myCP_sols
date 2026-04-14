from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        sentinel = TreeNode(val=-(10**9), left=None, right=root)

        curr = root
        prev = sentinel

        while curr:
            if key < curr.val:
                prev = curr
                curr = curr.left
            elif key > curr.val:
                prev = curr
                curr = curr.right
            else:
                is_left = prev.left == curr
                if curr.left is None or curr.right is None:
                    self._assign_to_parent(
                        prev, curr.right if curr.left is None else curr.left, is_left
                    )
                else:
                    successor = self.get_smallest_node(curr.right)
                    successor.left = curr.left
                    self._assign_to_parent(prev, curr.right, is_left)
                break

        return sentinel.right

    @staticmethod
    def get_smallest_node(node: TreeNode) -> TreeNode:
        curr = node

        while curr and curr.left:
            curr = curr.left

        return curr

    @staticmethod
    def _assign_to_parent(parent: TreeNode, child: TreeNode, is_left: bool):
        if is_left:
            parent.left = child
        else:
            parent.right = child
