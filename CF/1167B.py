def find_common(x, y):
    if x[0] in set(y):
        return x[0]
    return x[1]


def func(products):
    ans = [-1] * 6
    ind = 1
    for _ in range(2):
        print('? {} {}'.format(ind, ind + 1))
        a = int(input())
        t1 = products[a]
        print('? {} {}'.format(ind + 1, ind + 2))
        b = int(input())
        t2 = products[b]
        ans[ind] = find_common(t1, t2)
        ans[ind - 1] = a // ans[ind]
        ans[ind + 1] = b // ans[ind]
        ind = 4
    print('! {} {} {} {} {} {}'.format(*ans))


if __name__ == '__main__':
    ar = [4, 8, 15, 16, 23, 42]
    prods = {}
    for i in ar:
        for j in ar:
            prods[i * j] = (i, j)
    func(prods)
