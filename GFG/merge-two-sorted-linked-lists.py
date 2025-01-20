from typing import Optional


class Node:
    def __init__(self, data):  # data -> value stored in node
        self.data = data
        self.next = None


class Solution:
    def sortedMerge(
        self, head1: Optional[Node], head2: Optional[Node]
    ) -> Optional[Node]:
        dummy = Node(-float("inf"))
        head = dummy

        while head1 and head2:
            if head1.data <= head2.data:
                head.next = head1
                head1 = head1.next
            else:
                head.next = head2
                head2 = head2.next
            head = head.next
            head.next = None

        rem_head = head1 if head1 else head2

        while rem_head:
            head.next = rem_head
            rem_head = rem_head.next
            head = head.next
            head.next = None

        return dummy.next
