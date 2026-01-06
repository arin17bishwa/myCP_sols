from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q=deque([root])

        curr_lvl=0
        ans=1
        curr_mx=-(10**9)

        while q:
            lvl_sum=0
            curr_lvl+=1
            for _ in range(len(q)):
                node=q.popleft()
                lvl_sum+=node.val

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

            if lvl_sum>curr_mx:
                ans=curr_lvl
                curr_mx=lvl_sum

        return ans

