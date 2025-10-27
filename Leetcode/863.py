from collections import deque
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parents: dict[TreeNode, TreeNode | None] = {root: None}

        def dfs(node: TreeNode | None):
            nonlocal parents
            if not node:
                return
            if node.left:
                parents[node.left] = node
            if node.right:
                parents[node.right] = node

            dfs(node.left)
            dfs(node.right)

        dfs(root)

        vis = set()

        q = deque([target])

        dist = 0
        while q and dist < k:
            for _ in range(len(q)):
                curr = q.popleft()
                if not curr or curr in vis:
                    continue
                vis.add(curr)

                if curr.left and curr.left not in vis:
                    q.append(curr.left)
                if curr.right and curr.right not in vis:
                    q.append(curr.right)
                if parents[curr] and parents[curr] not in vis:
                    q.append(parents[curr])

            dist += 1
        return [i.val for i in q if i]
