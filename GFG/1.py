# dp = {1: 1}
#
#
# def sum_dig(n):
#     return sum(map(int, str(n)))
#
#
# def pre_comp():
#     global dp
#     n = 10 ** 5 + 5
#
#     for i in range(0, 2 * n, 2):
#         x = sum_dig(i) + sum_dig(i + 1)
#         if x in dp:
#             continue
#         dp[x] = i
#
#
# def solve(S):
#     # Write your code here
#     n = S
#     return dp.get(n, -1)
#
#
# if __name__ == '__main__':
#     T = int(input())
#     pre_comp()
#     print(sorted(dp.items()))
#     for _ in range(T):
#         S = int(input())
#
#         out_ = solve(S)
#         print(out_)


def func(_xor, _and, idx=0, a=0, b=0):
    global ans
    print(_xor, _and, idx, a, b)
    for i in range(idx, 64):
        xi = bool(_xor & (1 << i))
        ai = bool(_and & (1 << i))
        # print(i, xi, ai)
        if xi == ai == 0:
            pass
        elif xi == 0 and ai == 1:
            pass
        elif xi == 1 and ai == 0:
            func(_xor, _and, i + 1, a, b | (1 << i))
            a |= 1 << i
    ans.add((a + 1, b + 1))
    ans.add((b + 1, a + 1))


def solve(n):
    # Write your code here
    global ans
    _xor = n >> 1
    _and = (n - _xor) >> 1
    for i in range(64):
        if (_xor & (1 << i)) == (_and & (1 << i)) == 1:
            return [(-1, -1)]
    func(_xor, _and)
    if (0, 0) in ans:
        ans.remove((0, 0))
    return sorted(ans)


if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        N = int(input())
        ans = set()
        out_ = solve(N)
        for i_out_ in out_:
            print(' '.join(map(str, i_out_)))
