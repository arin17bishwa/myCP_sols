def func(n, l):
    s = 0
    for i in range(1, n):
        s += abs(l[i] - l[i - 1]) - 1
    return s


def main():
    st = ""
    for _ in range(int(input())):
        n = int(input())
        l = list(map(int, input().split()))
        st += str(func(n, l)) + "\n"
    print(st)


main()
