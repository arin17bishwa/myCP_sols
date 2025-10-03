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
        sentry: ListNode = ListNode()
        curr = sentry
        h1, h2 = l1, l2
        carry: int = 0
        while h1 and h2:
            sm = h1.val + h2.val + carry
            curr.next = ListNode(sm % 10)
            carry = sm // 10
            curr = curr.next
            h1 = h1.next
            h2 = h2.next
        if h1:
            remaining = h1
        elif h2:
            remaining = h2
        else:
            remaining = None

        while remaining:
            sm = remaining.val + carry
            curr.next = ListNode(sm % 10)
            carry = sm // 10
            curr = curr.next
            remaining = remaining.next

        if carry:
            curr.next = ListNode(carry)

        return sentry.next


def to_ll(arr: list[int]) -> Optional[ListNode]:
    if not arr:
        return None
    sentry = ListNode()
    curr = sentry
    for i in arr:
        curr.next = ListNode(i)
        curr = curr.next
    return sentry.next


def print_ll(head: Optional[ListNode]):
    arr = []
    while head:
        arr.append(head.val)
        head = head.next
    print(arr)


def main():
    obj = Solution()

    l1 = [2, 4, 3]
    l2 = [5, 6, 4]

    l1 = [0]
    l2 = [0]

    l1 = [9, 9, 9, 9, 9, 9, 9]
    l2 = [9, 9, 9, 9]
    ans = obj.addTwoNumbers(to_ll(l1), to_ll(l2))

    print_ll(ans)


if __name__ == "__main__":
    main()
