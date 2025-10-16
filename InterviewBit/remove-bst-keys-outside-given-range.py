class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


class Solution:
    def removekeys(self, root, l, r):
        def func(node: Node | None) -> Node | None:
            if not node:
                return
            node.left = func(node.left)
            node.right = func(node.right)

            if l <= node.data <= r:
                return node
            if node.data < l:
                return node.right
            else:
                return node.left

        return func(root)
