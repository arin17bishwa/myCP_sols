# cook your dish here

st = ''


def func(n, s):
    t = ''
    l = []
    for i in s:
        if i == 'L':
            l.append(-1)
        elif i == 'R':
            l.append(1)
        elif i == 'U':
            l.append(2)
        else:
            l.append(-2)
    i = 0
    # print(l)
    while i < n:
        t += s[i]
        if l[i] % 2 == 0:
            while i < n - 1 and l[i + 1] % 2 == 0:
                i += 1
                continue
        else:
            while i < n - 1 and l[i + 1] & 1 != 0:
                i += 1
                continue
        i += 1
    x, y = 0, 0
    for i in t:
        if i == 'L':
            x -= 1
        elif i == 'R':
            x += 1
        elif i == 'U':
            y += 1
        else:
            y -= 1
    # print(t)
    return (str(x) + ' ' + str(y))


for _ in range(int(input())):
    # n,name=map(str,input().split())
    n = int(input())
    # l1=[]
    # inp=input().split()
    s = input()
    # l1=list(map(int,input().split()))
    # l2 = list(map(int, input().split()))
    # l1=input().split()
    # l2=input().split()
    st += str(func(n, s)) + '\n'

print(st)
