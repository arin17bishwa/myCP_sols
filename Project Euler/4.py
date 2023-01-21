def isPalindrome(n: int):
    s = str(n)
    return s == s[::-1]


def solve(low=100, high=1000):
    ans = 1
    a = high - 1
    while a >= low:
        if a % 11 == 0:
            b = 999
            step = 1
        else:
            b = 990
            step = 11
        while b >= a:
            if a * b <= ans:
                break
            if isPalindrome(a * b):
                ans = max(ans, a * b)
            b -= step
        a -= 1
    return ans


if __name__ == '__main__':
    answer = solve()
    print(answer)
