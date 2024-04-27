# cook your dish here
def func(s):
    tot = 0
    i = 0
    len1 = len(s)
    if len1 < 3:
        return "NO"
    while i < len1:
        j = i
        if j == len1:
            break
        c = 0
        # print(s[i],s[j])
        while s[i] == s[j]:
            c += 1
            j += 1
            if j == len1:
                break
        i = j
        tot = tot + len(str(c)) + 1
    # print(s,tot,len1)
    if tot < len1:
        return "YES"
    return "NO"


st = ""
for _ in range(int(input())):
    s = input()
    st = st + func(s) + "\n"
print(st)
