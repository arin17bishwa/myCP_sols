class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return f"{self.data}->{self.next}"


class Solution:
    def mergeSort(self, head: Node) -> Node:
        def find_mid(node: Node) -> Node:
            slow = node
            fast = node
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            ans = slow.next
            slow.next = None
            return ans

        def merge(h1: Node, h2: Node) -> Node:
            sentry = Node(0)
            curr = sentry
            while h1 and h2:
                if h1.data <= h2.data:
                    curr.next = h1
                    h1 = h1.next
                else:
                    curr.next = h2
                    h2 = h2.next
                curr = curr.next
            if h1:
                curr.next = h1
            if h2:
                curr.next = h2
            return sentry.next

        def merge_sort(node: Node) -> Node:
            sentry = Node(0)
            curr = sentry
            mid = find_mid(node)
            if mid is None:
                if node.next and node.data > node.next.data:
                    node.data, node.next.data = node.next.data, node.data
                return node

            h1, h2 = merge_sort(node), merge_sort(mid)
            return merge(h1, h2)

        return merge_sort(head)


def make_ll(arr: list[int]) -> Node:
    nodes = [Node(i) for i in arr]
    for i in range(1, len(arr)):
        nodes[i - 1].next = nodes[i]
    return nodes[0]


def print_ll(head: Node):
    arr = []
    while head:
        arr.append(head.data)
        head = head.next
    print(arr)


def main():
    obj = Solution()

    arr = list(range(5))

    arr = list(map(int, "3 5 2 4 1".split()))

    h1 = make_ll(arr)
    ans = obj.mergeSort(h1)
    print(ans)
    print(print_ll(ans))


if __name__ == "__main__":
    main()
