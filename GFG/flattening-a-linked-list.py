import heapq


class Node:
    def __init__(self, d):
        self.data = d
        self.next = None
        self.bottom = None


class Solution:
    def flatten(self, root: Node) -> Node:
        heap: list[tuple[int, int, Node]] = []
        dummy = Node(0)
        curr = root
        it = iter(range(10**9))
        while curr:
            heapq.heappush(heap, (curr.data, next(it), curr))
            curr = curr.next

        curr = dummy

        while heap:
            _, _, node = heapq.heappop(heap)
            curr.bottom = node

            if node.bottom:
                t = node.bottom
                heapq.heappush(heap, (t.data, next(it), t))
                node.bottom = None
            curr = curr.bottom
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