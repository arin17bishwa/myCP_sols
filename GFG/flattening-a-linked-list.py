from typing import Optional


class Node:
    def __init__(self, d):
        self.data = d
        self.next = None
        self.bottom = None


class Solution:
    def flatten(self, root: Node) -> Optional[Node]:
        if not root or not root.next:
            return root
        root.next = self.flatten(root.next)
        root.next = self.merge(root, root.next)
        return root

    @staticmethod
    def merge(h1: Optional[Node], h2: Optional[Node]) -> Optional[Node]:
        dummy = Node(0)
        curr = dummy
        while h1 and h2:
            if h1.data <= h2.data:
                curr.bottom = h1
                h1 = h1.bottom
            else:
                curr.bottom = h2
                h2 = h2.bottom
            curr = curr.bottom
        if h1:
            curr.bottom = h1
        elif h2:
            curr.bottom = h2
        return dummy.bottom


def print_ll_custom(head: Node):
    arr = []
    while head:
        col = []
        curr = head
        while curr:
            col.append(curr.data)
            curr = curr.bottom
        arr.append(col[:])
        head = head.next

    print(arr)


def matrix_to_custom_ll(mat: list[list[int]]) -> Node:
    dummy = Node(0)
    curr = dummy

    for col in mat:
        it = iter(col)
        top = Node(next(it))
        t = top
        for v in it:
            t.bottom = Node(v)
            t = t.bottom
        curr.next = top
        curr = curr.next
    return dummy.next


def print_ll(head: Node):
    arr = []
    while head:
        arr.append(head.data)
        head = head.bottom
    print(arr)


def main():
    obj = Solution()

    arr = [[5, 7, 8], [10, 20], [19, 20], [28, 40, 45]]

    # print_ll_custom(matrix_to_custom_ll(arr))
    head = matrix_to_custom_ll(arr)

    ans = obj.flatten(head)

    # print_ll(ans)


if __name__ == "__main__":
    main()
