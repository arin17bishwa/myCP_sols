n = int(input())
s = input()
l = list(s)
i = ans = j = 0

while i < n - 1:
    if s[i] == s[i + 1]:
        ans += 1
    i += 1

print(min(ans, n - 1))
