class Solution:
    def largestSwap(self, s: str) -> str:
        arr = list(s)
        n = len(arr)

        occ = [-1] * 10
        for i in range(n):
            occ[int(arr[i])] = i

        swapped = False
        for i in range(n):
            for j in range(9, int(arr[i]), -1):
                if occ[j] == -1 or occ[j] < i:
                    continue
                arr[i], arr[occ[j]] = arr[occ[j]], arr[i]
                swapped = True
                break
            if swapped:
                break

        return "".join(arr)


def main():
    obj = Solution()

    s = "768"
    # s = "333"
    # s='3033'
    s = "10"

    ans = obj.largestSwap(s)

    # print(ans)


if __name__ == "__main__":
    main()
