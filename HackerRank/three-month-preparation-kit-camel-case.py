def intArr():
    return map(int, input().split())


def In():
    return int(input())


def func():
    todo, what, s = input().strip().split(';')
    if todo == 'C':
        s = s.split()
        n = len(s)
        for i in range(1, n):
            s[i] = s[i].capitalize()
        if what == 'C':
            s[0] = s[0].capitalize()
        return ''.join(s) + ('' if what != 'M' else '()')
    if what == 'M':
        s = s[:len(s) - 2]
    arr = [i.isupper() for i in s]
    curr = []
    ans = []
    for i, j in enumerate(arr):
        if j:
            if curr:
                ans.append(''.join(curr))
            curr = [s[i].lower()]
        else:
            curr.append(s[i])
    if curr:
        ans.append(''.join(curr))
    return ' '.join(ans)


def main():
    while 1:
        try:
            print(func())
        except EOFError:
            break
    return


if __name__ == '__main__':
    main()
