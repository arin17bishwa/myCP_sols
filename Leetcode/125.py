class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        head, tail = 0, n - 1
        while head < tail:
            while head < tail and not s[head].isalnum():
                head += 1
            while head < tail and not s[tail].isalnum():
                tail -= 1
            if head == tail:
                return True
            if s[head].lower() != s[tail].lower():
                return False
            head += 1
            tail -= 1
        return True
