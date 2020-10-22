# region smaller_fastio
from sys import stdin,stdout
from os import path


if (path.exists('input.txt')):
    #------------------Sublime--------------------------------------#
    stdin=open('input.txt','r');stdout=open('output.txt','w');
    def I():return (int(input()))
    def In():return(map(int,input().split()))
else:
    #------------------PYPY FAst I/o--------------------------------#
    def I():return (int(stdin.readline()))
    def In():return(map(int,stdin.readline().split()))

#endregion
import heapq,random


cout=stdout.write
def func(q):
    n=q#I()
    st=''
    med=0
    max_heap=[]
    min_heap=[]
    for i in range(1,n+1):
        k=random.randint(1,10**6)#I()
        if len(max_heap)>len(min_heap):
            if k<med:
                x=heapq.heapreplace(max_heap,(-k,k))
                heapq.heappush(min_heap,(-x[0],x[1]))
            else:
                heapq.heappush(min_heap,(k,k))
            med = (max_heap[0][1] + min_heap[0][1]) // 2

        elif len(max_heap)<len(min_heap):
            if k<med:
                heapq.heappush(max_heap,(-k,k))
            else:
                x=heapq.heapreplace(min_heap,(k,k))
                heapq.heappush(max_heap,(-x[0],x[1]))
            med = (max_heap[0][1] + min_heap[0][1]) // 2

        else:
            if k<med:
                heapq.heappush(max_heap,(-k,k))
                med=max_heap[0][1]
            else:
                heapq.heappush(min_heap,(k,k))
                med=min_heap[0][1]

        st='\n'.join((st,str(med)))
    cout(st.lstrip())

if __name__ == '__main__':
    x=random.randint(1,10**6)
    print(x)
    func(x)