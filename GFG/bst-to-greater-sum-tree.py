class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


class Solution:
    def transformTree(self, root: Node):

        def func(node: Node | None, carry: int = 0):
            if not node:
                return 0
            curr = node.data
            right = func(node.right, carry)
            left = func(node.left, carry + curr + right)
            node.data = right + carry
            return right + left + curr

        func(root)
        return root
