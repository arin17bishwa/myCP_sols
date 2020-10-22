st = ''


def func(l):
    d = {5: 0, 10: 0, 15: 0}
    for coin in l:
        d[coin] += 1
        c = coin - 5
        if c == 0:
            continue
        elif c == 5:
            if d[5] > 0:
                d[5] -= 1
            else:
                return 'NO'
        elif c == 10:
            if d[10] > 0:
                d[10] -= 1
            elif d[5] > 1:
                d[5] -= 1
            else:
                return 'NO'
    return 'YES'


for _ in range(int(input())):
    n = int(input())
    l1 = list(map(int, input().split()))
    st += str(func(l1)) + '\n'
print(st)
