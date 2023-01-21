n=int(input())
s1=sum(list(map(int,input().split())))
s2=sum(list(map(int,input().split())))
ans1=s1-s2
ans2=s2-sum(list(map(int,input().split())))
print(ans1,'\n'+str(ans2))