def solve(n):
    lim = int(pow(n, 0.5) + 1)
    ans = 1
    if n & 1 == 0:
        ans = 2
        while n & 1 == 0:
            n >>= 1

    for i in range(3, lim + 1, 2):
        if n % i == 0:
            ans = i
            while n % i == 0:
                n //= i
        if n == 1:
            return ans
    return max(ans, n)


if __name__ == '__main__':
    answer = solve(n=600851475143)
    print(answer)
