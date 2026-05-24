from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        carry: int = 0
        ans: ListNode = ListNode(0)
        curr = ans
        h1, h2 = l1, l2

        while h1 and h2:
            current_sm: int = carry + h1.val + h2.val
            curr.next = ListNode(current_sm % 10)
            curr = curr.next
            carry = current_sm // 10
            h1 = h1.next
            h2 = h2.next

        residual=h1 or h2

        while residual:
            current_sm = carry + residual.val
            curr.next = ListNode(current_sm % 10)
            curr = curr.next
            residual = residual.next
            carry = current_sm // 10

        if carry:
            curr.next = ListNode(carry)

        return ans.next
