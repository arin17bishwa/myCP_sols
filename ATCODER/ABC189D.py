n = int(input())
arr = [input() for _ in range(n)]
dp = [1] * (n + 1)
for i in range(1, n + 1):
    dp[i] = dp[i - 1]
    if arr[i - 1] == 'OR':
        dp[i] += 1 << i
print(dp[n])
