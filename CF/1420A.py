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

def mergeSort(arr, n):
    # A temporary_Array is created to store
    # sorted array in merge function
    temporary_Array = [0] * n
    return _mergeSort(arr, temporary_Array, 0, n - 1)



def _mergeSort(arr, temporary_Array, left, right):
    # A variable inv_count is used to store
    # inversion counts in each recursive call

    inv_count = 0

    # We will make a recursive call if and only if
    # we have more than one elements

    if left < right:
        # mid is calculated to divide the array into two subarrays
        # Floor division is must in case of python

        mid = (left + right) // 2

        # It will calculate inversion counts in the left subarray

        inv_count += _mergeSort(arr, temporary_Array, left, mid)

        # It will calculate inversion counts in right subarray

        inv_count += _mergeSort(arr, temporary_Array, mid + 1, right)


        inv_count += merge(arr, temporary_Array, left, mid, right)
    return inv_count


def merge(arr, temporary_Array, left, mid, right):
    i = left  #
    j = mid + 1
    k = left
    inv_count = 0


    while i <= mid and j <= right:


        if arr[i] <= arr[j]:
            temporary_Array[k] = arr[i]
            k += 1
            i += 1
        else:
            temporary_Array[k] = arr[j]
            inv_count += (mid - i + 1)
            k += 1
            j += 1

    while i <= mid:
        temporary_Array[k] = arr[i]
        k += 1
        i += 1

    while j <= right:
        temporary_Array[k] = arr[j]
        k += 1
        j += 1

    return inv_count

def main():
    t=I()
    st=''
    for _ in range(t):
        n=I()
        l=list(In())
        k=mergeSort(l,n)
        if k<=(((n-1)*n)/2)-1:
            ans='YES'
        else:
            ans='NO'
        st='\n'.join((st,ans))
    print(st[1:])
if __name__ == '__main__':
    main()