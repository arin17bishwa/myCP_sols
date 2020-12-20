if __name__ == '__main__':
    t = int(input())
    ans = [0] * t
    for i in range(t):
        n = int(input())
        ans[i] = (n * (n + 2) * (1 + (n << 1)) >> 3)
    print('\n'.join(map(str, ans)))
