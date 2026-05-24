class Solution:
    def passwordStrength(self, password: str) -> int:
        s: set[str] = set(password)
        ans = 0

        for ch in s:
            if ch.isalpha():
                if ch.islower():
                    ans += 1
                else:
                    ans += 2
            elif ch.isnumeric():
                ans += 3
            elif ch in "!@#$":
                ans += 5

        return ans
