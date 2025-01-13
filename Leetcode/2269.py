class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        s = str(num)
        n = len(s)
        ans = 0
        for i in range(n - k + 1):
            sub_str = s[i: i + k]
            if sub_str.count("0") < k and num % int(sub_str) == 0:
                ans += 1
        return ans
