from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: "Node") -> List[int]:
        ans: List[int] = []

        def dfs(node: Node, arr: List[int]):
            if not node:
                return
            for child in node.children:
                dfs(child, arr)
            arr.append(node.val)

        dfs(root, ans)
        return ans
