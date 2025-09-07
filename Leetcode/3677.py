class Solution:
    def countBinaryPalindromes(self, n: int) -> int:
        if n == 0:
            return 1

        cnt = 1
        m = n.bit_length()

        for length in range(1, m):
            cnt += 1 << (((length + 1) >> 1) - 1)

        half = (m + 1) // 2
        prefix = n >> (m - half)

        def make_palindrome(_prefix):
            nonlocal m
            if m % 2 == 0:
                left = _prefix
                right = int(bin(_prefix)[2:][::-1], 2)
            else:
                left = _prefix
                right = int(bin(_prefix >> 1)[2:][::-1], 2)
            return (left << (m // 2)) | right

        pal = make_palindrome(prefix)

        base = 1 << (half - 1)
        cnt += prefix - base
        if pal <= n:
            cnt += 1

        return cnt
