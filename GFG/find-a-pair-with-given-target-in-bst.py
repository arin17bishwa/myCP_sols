from typing import Optional, List


class Node:
    def __init__(self, val: int):
        self.right: Optional[Node] = None
        self.data = val
        self.left: Optional[Node] = None


class Solution:
    def findTarget(self, root: Optional[Node], target: int) -> bool:

        arr: List[int] = []

        def dfs(node: Optional[Node]):
            if not node:
                return
            dfs(node.left)
            arr.append(node.data)
            dfs(node.right)

        dfs(root)
        n = len(arr)
        i, j = 0, n - 1
        while i < j:
            x = arr[i] + arr[j]
            if x < target:
                i += 1
            elif x > target:
                j -= 1
            else:
                return True
        return False
