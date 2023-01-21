just = {2: 4, 3: 4, 4: 2, 5: 1, 6: 1, 7: 4, 8: 4, 9: 2}


def func(a, b):
    if a == 0:
        return 0
    if b == 0 or a == 1:
        return 1
    b = b % just[a]
    if b == 0:
        b = just[a]
    return pow(a, b, 10)


if __name__ == '__main__':
    t = int(input())
    answers = [' '] * t
    for i in range(t):
        x, y = map(int, input().split())
        answers[i] = str(func(x % 10, y))
    print('\n'.join(answers))
