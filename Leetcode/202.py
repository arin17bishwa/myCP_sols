class Solution:
    def isHappy(self, n: int) -> bool:
        def transform(p: int) -> int:
            return sum(map(lambda x: pow(int(x), 2), str(p)))

        seen: set[int] = set()

        if n == 1:
            return True
        if n <= 3:
            return False

        while True:
            t = transform(n)
            if t == 1:
                return True
            elif t <= 3:
                return False
            elif t in seen:
                return False
            else:
                seen.add(t)
                n = t
