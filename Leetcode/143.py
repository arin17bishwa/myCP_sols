from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val: int = val
        self.next: Optional[ListNode] = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if (not head) or (not head.next):
            return

        slow = fast = head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        prev.next = None

        t1 = head
        t2 = self.reverse(slow)

        curr_t1 = t1
        curr_t2 = t2
        dummy: ListNode = ListNode(0)
        curr = dummy

        while curr_t1 and curr_t2:
            curr.next = curr_t1
            curr_t1 = curr_t1.next

            curr.next.next = curr_t2
            curr_t2 = curr_t2.next

            curr = curr.next.next

        if curr_t2:
            curr.next = curr_t2

        head = dummy.next

    @staticmethod
    def reverse(head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        prev: Optional[ListNode] = None
        curr: Optional[ListNode] = head
        while curr:
            t = curr.next
            curr.next = prev
            prev = curr
            curr = t
        return prev
