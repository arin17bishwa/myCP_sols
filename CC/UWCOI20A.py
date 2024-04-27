s = ""

for _ in range(int(input())):
    m = -1
    for _ in range(int(input())):
        m = max(m, int(input()))
    s += str(m) + "\n"

print(s)
