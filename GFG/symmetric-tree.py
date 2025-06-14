class Node:
    def __init__(self, val: int):
        self.right = None
        self.data = val
        self.left = None


class Solution:
    def isSymmetric(self, root: Node) -> bool:

        def dfs(left_node: Node, right_node: Node) -> bool:
            if (left_node, right_node).count(None) % 2:
                return False
            if left_node is None:
                return True
            return (
                left_node.data == right_node.data
                and dfs(left_node.left, right_node.right)
                and dfs(left_node.right, right_node.left)
            )

        return dfs(root.left, root.right)
