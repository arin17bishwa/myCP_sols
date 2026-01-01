class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def len_ll(head: Node) -> int:
    curr = head
    ans = 0
    while curr:
        ans += 1
        curr = curr.next
    return ans


class Solution:
    def intersectPoint(self, head1: Node, head2: Node) -> Node:
        l1 = len_ll(head1)
        l2 = len_ll(head2)

        if l1 <= l2:
            for _ in range(l2 - l1):
                head2 = head2.next
        else:
            for _ in range(l1 - l2):
                head1 = head1.next

        while head1 != head2:
            head1 = head1.next
            head2 = head2.next

        return head1
