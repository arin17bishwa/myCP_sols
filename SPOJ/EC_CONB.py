if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        if n & 1:
            print(n)
        else:
            b = bin(n)[2::]
            print(int(b[::-1], 2))
