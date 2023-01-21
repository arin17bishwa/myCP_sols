def get_val(i):
    print('? {}'.format(i + 1))
    p = int(input())
    return p


def bin_src(low, high, n):
    global arr
    mid = 1
    while low <= high:
        mid = (high + low) >> 1

        if mid > 0 and arr[mid - 1] == -1:
            arr[mid - 1] = get_val(mid - 1)
        if mid + 1 < n and arr[mid + 1] == -1:
            arr[mid + 1] = get_val(mid + 1)
        if arr[mid] == -1:
            arr[mid] = get_val(mid)

        if (mid == 0 or arr[mid - 1] > arr[mid]) and (mid == n - 1 or arr[mid] < arr[mid + 1]):
            return mid

        elif mid > 0 and arr[mid - 1] < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return mid


def main():
    global arr
    n = int(input())
    if n == 1:
        print('! 1')
        return
    arr = [-1] * n
    ans = bin_src(0, n - 1, n) + 1
    print('! {}'.format(ans))
    return


if __name__ == '__main__':
    arr = []
    main()
