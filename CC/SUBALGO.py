n, a = map(int, input().split())
i = 0
while i < a and n > 0:
    if n % 10 == 0:
        n = n // 10
    else:
        n -= 1
    i += 1
print(n)
