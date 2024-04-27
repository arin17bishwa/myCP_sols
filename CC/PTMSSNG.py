def func(xd, yd):
    x = y = 0
    for k, v in xd.items():
        if v:
            x = k
            break
    for k, v in yd.items():
        if v:
            y = k
            break
    return " ".join((str(x), str(y)))


def main():
    st = ""
    for _ in range(int(input())):
        n = int(input())
        xd = dict()
        yd = dict()
        for _ in range(4 * n - 1):
            a, b = map(int, input().split())
            xd[a] = (xd.get(a, 0) + 1) % 2
            yd[b] = (yd.get(b, 0) + 1) % 2
        st = "\n".join((st, str(func(xd, yd))))
    print(st[1:])


main()
