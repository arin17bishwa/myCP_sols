from typing import Optional, List, Set


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def modifiedList(
        self, nums: List[int], head: Optional[ListNode]
    ) -> Optional[ListNode]:
        nums_set: Set[int] = set(nums)
        dummy = ListNode(0, head)
        curr: Optional[ListNode] = dummy.next
        prev: Optional[ListNode] = dummy
        while curr:
            if curr.val in nums_set:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        return dummy.next
