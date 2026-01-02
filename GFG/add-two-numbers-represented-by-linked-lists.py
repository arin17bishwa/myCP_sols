from typing import Optional


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def reverse(head: Optional[Node]) -> Optional[Node]:
    if not head:
        return None

    prev = None
    curr = head
    while curr:
        t = curr.next
        curr.next = prev
        prev = curr
        curr = t

    return prev


class Solution:
    def addTwoLists(self, head1, head2):
        h1 = reverse(head1)
        h2 = reverse(head2)
        dummy = Node(0)
        curr = dummy
        carry = 0
        while h1 and h2:
            sm = h1.data + h2.data + carry
            curr.next = Node(sm % 10)
            curr = curr.next
            h1 = h1.next
            h2 = h2.next
            carry = sm // 10

        while h1:
            sm = h1.data + carry
            curr.next = Node(sm % 10)
            curr = curr.next
            h1 = h1.next
            carry = sm // 10

        while h2:
            sm = h2.data + carry
            curr.next = Node(sm % 10)
            curr = curr.next
            h2 = h2.next
            carry = sm // 10

        if carry:
            curr.next = Node(carry)

        dummy.next = reverse(dummy.next)

        while dummy.next and dummy.next.data == 0:
            dummy.next = dummy.next.next
        return dummy.next


def list_to_ll(arr: list[int]) -> Node:
    n = len(arr)
    ans = [Node(i) for i in arr]
    for i in range(n - 1):
        ans[i].next = ans[i + 1]
    return ans[0]


def print_ll(head: Optional[Node]):
    ans = []
    while head:
        ans.append(head.data)
        head = head.next
    print(*ans, sep="->")


def main():
    obj = Solution()

    a1 = [1, 2, 3]
    a2 = [9, 9, 9]

    a1 = [0, 0, 6, 3]
    a2 = [0, 7]

    h1 = list_to_ll(a1)
    h2 = list_to_ll(a2)
    ans = obj.addTwoLists(h1, h2)
    # print_ll(ans)


if __name__ == "__main__":
    main()
