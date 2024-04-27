st = ''


def func(n, s, d):
    a = d[0] + d[1]
    if s + a > 100:
        return 'no'
    return 'yes'


for _ in range(int(input())):
    d = {0: 1000, 1: 1000}
    n, s = map(int, input().split())
    l1 = list(map(int, input().split()))
    l2 = list(map(int, input().split()))
    for i in range(n):
        if l2[i] == 0:
            d[0] = min(d[0], l1[i])
        else:
            d[1] = min(d[1], l1[i])
    st = st + str(func(n, s, d)) + '\n'
print(st)
