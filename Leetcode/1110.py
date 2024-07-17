from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def delNodes(
        self, root: Optional[TreeNode], to_delete: List[int]
    ) -> List[TreeNode]:
        to_delete_set: set = set(to_delete)
        orphan_nodes: List[TreeNode] = []

        def dfs(node: Optional[TreeNode]) -> Optional[TreeNode]:
            nonlocal orphan_nodes, to_delete

            if not node:
                return
            node.left = dfs(node.left)
            node.right = dfs(node.right)
            if node.val in to_delete_set:
                if node.left:
                    orphan_nodes.append(node.left)
                if node.right:
                    orphan_nodes.append(node.right)
                return
            return node

        root = dfs(root)

        if root:
            orphan_nodes.append(root)
        return orphan_nodes
