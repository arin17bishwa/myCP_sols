class Solution:
    def andInRange(self, l: int, r: int):
        shift: int = 0

        while l != r:
            l >>= 1
            r >>= 1
            shift += 1
        return l << shift
