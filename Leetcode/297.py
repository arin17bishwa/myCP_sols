from collections import deque


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    SEP = "#"
    NULL_PLACEHOLDER = "n"

    def serialize(self, root: TreeNode | None) -> str:
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""

        ans: list[str] = [str(root.val)]
        q: deque[TreeNode] = deque([root])

        while q:
            curr = q.popleft()

            for v in (curr.left, curr.right):
                if v is not None:
                    ans.append(str(v.val))
                    q.append(v)
                else:
                    ans.append(self.NULL_PLACEHOLDER)

        return self.SEP.join(ans)

    def deserialize(self, data: str) -> TreeNode | None:
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        def create_node(s: str) -> TreeNode | None:
            if s[0] == self.NULL_PLACEHOLDER:
                return None
            return TreeNode(int(s))

        if not data:
            return None

        input_q: deque[str] = deque(data.split(self.SEP))

        root = create_node(input_q.popleft())

        curr_q: deque[TreeNode] = deque([root])

        while curr_q:
            curr = curr_q.popleft()
            left = create_node(input_q.popleft())
            right = create_node(input_q.popleft())
            if left:
                curr.left = left
                curr_q.append(left)
            if right:
                curr.right = right
                curr_q.append(right)
        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
