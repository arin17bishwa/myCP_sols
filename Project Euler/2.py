def func():
    n = 4000000
    l = [0, 1, 2]
    while l[-1] < n:
        l.append(l[-1] + l[-2])
    print(sum(l[2::3]))


if __name__ == '__main__':
    func()
