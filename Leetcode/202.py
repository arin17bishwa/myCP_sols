class Solution:
    def isHappy(self, n: int) -> bool:
        def transform(p: int) -> int:
            return sum(map(lambda x: pow(int(x), 2), str(p)))

        slow = transform(n)
        fast = transform(slow)

        while fast != 1:
            if fast == slow:
                return False
            slow = transform(slow)
            fast = transform(transform(fast))
        return True
