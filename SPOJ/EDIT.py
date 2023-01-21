def func(s):
    n = len(s)
    p = q = 0
    for i in range(n):
        if i & 1:
            if s[i].islower():
                p += 1
            else:
                q += 1
        else:
            if s[i].isupper():
                p += 1
            else:
                q += 1
    return min(p, q)


def main():
    while True:
        try:
            s = input()
            print(func(s))
        except Exception:
            break


if __name__ == '__main__':
    main()
