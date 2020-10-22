st = ''
for _ in range(int(input())):
    n = int(input())
    pr = 0
    for _ in range(n):
        s, p, v = map(int, input().split())
        pr = max(pr, (p // (s + 1)) * v)
    st += str(pr) + '\n'

print(st)
