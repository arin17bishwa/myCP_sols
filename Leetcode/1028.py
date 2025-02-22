from collections import deque
from typing import Optional, Deque, Tuple


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    # def __repr__(self):
    #     return f"({self.val}, {self.left.val if self.left else None}, {self.right.val if self.right else None})"


class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        split_traversal = traversal.split("-")
        m = len(split_traversal)
        root = TreeNode(int(split_traversal[0]))
        stack: Deque[Tuple[int, TreeNode]] = deque([(0, root)])
        curr_lvl: int = 1
        # print(split_traversal)
        for idx in range(1, m):
            node_val = split_traversal[idx]
            # print(stack)
            if node_val == "":
                curr_lvl += 1
                continue
            else:
                new_node = TreeNode(int(node_val))
                while stack and stack[-1][0] != curr_lvl - 1:
                    stack.pop()
                # print(curr_lvl, stack[-1], new_node)
                if stack:
                    parent_node: TreeNode = stack[-1][-1]
                    if parent_node.left:
                        parent_node.right = new_node
                    else:
                        parent_node.left = new_node
                    # print(
                    #     parent_node,
                    #     new_node,
                    # )
                stack.append((curr_lvl, new_node))
                curr_lvl = 1
        # print(root)
        return root


def main():
    obj = Solution()
    s = "1-2--3--4-5--6--7"
    s = "1-2--3--4-5--6--7"

    def bfs(node: TreeNode):
        fin = []
        q = deque([node])
        while q:
            curr = q.popleft()
            if not curr:
                continue
            fin.append(curr.val)
            q.append(curr.left)
            q.append(curr.right)
        return fin

    ans = obj.recoverFromPreorder(s)
    print(bfs(ans))


if __name__ == "__main__":
    main()
