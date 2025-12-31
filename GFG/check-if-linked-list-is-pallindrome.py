from typing import Optional


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def reverse_ll(head: Optional[Node]) -> Optional[Node]:
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


def find_mid_ll(head: Optional[Node]) -> Optional[Node]:
    if not head:
        return None

    fast = head
    slow = None

    while fast and fast.next:
        fast = fast.next.next
        if not slow:
            slow = head
        else:
            slow = slow.next
    return slow


class Solution:
    def isPalindrome(self, head: Optional[Node]) -> bool:
        if head is None or head.next is None:
            return True
        mid = find_mid_ll(head)
        h2 = mid.next
        mid.next = None
        h2 = reverse_ll(h2)
        h1 = head

        while h1 and h2:
            if h1.data != h2.data:
                return False
            h1 = h1.next
            h2 = h2.next

        return True


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

    arr = [1, 2, 1, 1, 2, 1]
    arr = [10, 20, 30, 40, 50]
    arr = [1, 1, 2, 1]

    head = list_to_ll(arr)

    ans = obj.isPalindrome(head)

    # print(ans)


if __name__ == "__main__":
    main()
