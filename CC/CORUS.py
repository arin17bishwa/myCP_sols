st = ""


def func():
    k = 0
    for i in freq:
        k += max(0, i - c)
    return k


for _ in range(int(input())):
    n, q = map(int, input().split())
    s = input()
    freq = [0 for _ in range(26)]
    for i in s:
        freq[ord(i) - ord("a")] += 1
    for _ in range(q):
        c = int(input())
        st += str(func()) + "\n"
    # freq=[]
print(st)
