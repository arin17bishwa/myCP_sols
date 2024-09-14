from typing import Optional
from math import gcd


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertGreatestCommonDivisors(
        self, head: Optional[ListNode]
    ) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        curr: Optional[ListNode] = head.next
        prev: ListNode = head
        while curr:
            hcf = gcd(prev.val, curr.val)
            new_node = ListNode(val=hcf, next=curr)
            prev.next = new_node
            prev, curr = curr, curr.next
        return head
