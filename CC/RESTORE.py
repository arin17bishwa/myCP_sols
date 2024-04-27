# region smaller_fastio
from sys import stdin, stdout


def I():
    return int(stdin.readline())


def In():
    return map(int, stdin.readline().split())


def S():
    return stdin.readline().rstrip()


def Sn():
    return stdin.readline().split(" ")


def Out(whatever):
    return stdout.write(whatever)


# endregion


# region sieve of Eratosthenes
def prime_sieve(n):
    """returns a sieve of primes >= 5 and < n"""
    flag = n % 6 == 2
    sieve = bytearray((n // 3 + flag >> 3) + 1)
    for i in range(1, int(n**0.5) // 3 + 1):
        if not (sieve[i >> 3] >> (i & 7)) & 1:
            k = (3 * i + 1) | 1
            for j in range(k * k // 3, n // 3 + flag, 2 * k):
                sieve[j >> 3] |= 1 << (j & 7)
            for j in range(k * (k - 2 * (i & 1) + 4) // 3, n // 3 + flag, 2 * k):
                sieve[j >> 3] |= 1 << (j & 7)
    return sieve


def prime_list(n):
    """returns a list of primes <= n"""
    res = []
    if n > 1:
        res.append(2)
    if n > 2:
        res.append(3)
    if n > 4:
        sieve = prime_sieve(n + 1)
        res.extend(
            3 * i + 1 | 1
            for i in range(1, (n + 1) // 3 + (n % 6 == 1))
            if not (sieve[i >> 3] >> (i & 7)) & 1
        )
    return res


# endregion


def func(n, arr):
    x = {}
    ans = [0] * n
    j = 0
    for i in range(n):
        if arr[i] not in x:
            ans[i] = PRIMES[j]
            x[arr[i]] = ans[i]
            j += 1
        else:
            ans[i] = x[arr[i]]
    return " ".join(map(str, ans))


if __name__ == "__main__":
    PRIMES = prime_list(pow(10, 6) << 2)
    t = I()
    answers = [" "] * t
    for i in range(t):
        size = I()
        ar = list(In())
        answers[i] = func(size, ar)
    Out("\n".join(answers))
