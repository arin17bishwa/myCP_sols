s=input()
i=ab=ba=0
n=len(s)
while i<n-1:
    if ab==0 and s[i]=='A' and s[i+1]=='B':
        ab=1
        i+=1
    elif ba==0 and s[i]=='B' and s[i+1]=='A':
        ba=1
        i+=1
    i+=1
if ab==1 and ba==1:
    print('YES')
else:
    s=s[::-1]
    i = ab = ba = 0
    n = len(s)
    while i < n - 1:
        if ba == 0 and s[i] == 'B' and s[i + 1] == 'A':
            ba = 1
            i += 1
        elif ab==0 and s[i]=='A' and s[i+1]=='B':
            ab = 1
            i += 1
        i += 1
    if ab==1 and ba==1:
        print('YES')
    else:
        print('NO')