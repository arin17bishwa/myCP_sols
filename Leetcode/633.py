class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        lo = 0
        hi = int(pow(c, 0.5))

        while lo <= hi:
            x = lo * lo + hi * hi

            if x > c:
                hi -= 1
            elif x < c:
                lo += 1
            else:
                return True
        return False
