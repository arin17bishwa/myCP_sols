st = ""


def func(n):
    s = ""
    l = [[0] * n for i in range(n)]
    e, o = False, True
    even, odd = 1, 2
    i = 0
    while i < n:
        j = 0
        while j < n:
            if o:
                l[i][j] = even
                even += 2
            else:
                l[i][j] = odd
                odd += 2
            e, o = o, e
            j += 1
        i += 1
        if n & 1 == 0:
            e, o = o, e
    for i in l:
        for j in i:
            s += str(j) + " "
        s += "\n"
    return s[:-1]


for _ in range(int(input())):
    n = int(input())
    st += str(func(n)) + "\n"
print(st)
