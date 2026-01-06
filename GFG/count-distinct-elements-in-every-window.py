from collections import defaultdict, Counter
class Solution:
    def countDistinct(self, arr:list[int], k:int)->list[int]:
        ans:list[int]=[]
        n=len(arr)
        freq:defaultdict[int,int]=defaultdict(int)

        for i in range(k):
            freq[arr[i]]+=1
        ans.append(len(freq))

        for i in range(k,n):
            freq[arr[i-k]]-=1
            freq[arr[i]]+=1
            if freq[arr[i-k]]==0:
                del freq[arr[i-k]]
            ans.append(len(freq))

        return ans