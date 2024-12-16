class Solution:

    def kthElement(self, a, b, k: int):
        return sorted(a + b)[k - 1]
