def func(i):
    return sum(int(d) for d in str(i))


def main():
    st = ''

    for _ in range(int(input())):
        chef = morty = 0
        n = int(input())
        for _ in range(n):
            a, b = map(func, input().split())
            if a > b:
                chef += 1
            elif a == b:
                chef += 1
                morty += 1
            else:
                morty += 1
        if chef > morty:
            ans = '0 ' + str(chef)
        elif morty == chef:
            ans = '2 ' + str(chef)
        else:
            ans = '1 ' + str(morty)
        st += str(ans) + '\n'
    print(st[:-1])


main()
