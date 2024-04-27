t = int(input())
s = ""
for i in range(t):
    a = "0"
    n = int(input())
    for j in range(n):
        a = str(bin(int(a, 2) ^ int((input()), 2)).replace("0b", ""))

    s = s + str(a.count("1")) + "\n"
print(s)
