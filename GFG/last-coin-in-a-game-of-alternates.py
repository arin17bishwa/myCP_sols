class Solution:
    def coin(self, arr:list[int])->int:
        n=len(arr)
        tail=n-1
        head=0
        while head<tail:
            if arr[head]>arr[tail]:
                head+=1
            else:
                tail-=1
        return arr[head]
