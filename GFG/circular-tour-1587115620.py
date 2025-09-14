class Solution:
    def startStation(self, gas: list[int], cost: list[int]):
        n = len(gas)

        start = 0

        while start < n:
            tank = 0
            curr = start
            while curr - start <= n:
                tank += gas[curr % n]
                if tank < cost[curr % n]:
                    start = curr + 1
                    break
                else:
                    tank -= cost[curr % n]
                curr += 1
            else:
                return start
        return -1


def main():
    obj = Solution()

    gas = [4, 5, 7, 4]
    cost = [6, 6, 3, 5]

    gas = [3, 9]
    cost = [7, 6]

    ans = obj.startStation(gas, cost)

    print(ans)


if __name__ == "__main__":
    main()
