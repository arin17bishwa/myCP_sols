class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        n = len(s)
        ones = [0] * n
        zeroes = ones[:]
        for i in range(n):
            if s[i] == "0":
                zeroes[i] += 1
            else:
                ones[i] += 1

        for i in range(1, n):
            zeroes[i] += zeroes[i - 1]
            ones[i] += ones[i - 1]
        ones.append(0)
        zeroes.append(0)
        ans = 0
        for start in range(n):
            for end in range(start, n):
                one = ones[end] - ones[start - 1]
                zero = zeroes[end] - zeroes[start - 1]
                if one <= k or zero <= k:
                    ans += 1
                elif one > k and zero > k:
                    break

        return ans
