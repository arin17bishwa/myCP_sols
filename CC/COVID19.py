st = ""


def func():
    m1, m2 = n, 0
    c = i = 1
    while i < n:
        if l[i] - l[i - 1] < 3:
            c += 1
        else:
            m1, m2 = min(m1, c), max(m2, c)
            c = 1
        i += 1
    m1, m2 = min(m1, c), max(m2, c)
    return str(m1) + " " + str(m2)


for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    # print(l)
    st += str(func()) + "\n"
print(st)
