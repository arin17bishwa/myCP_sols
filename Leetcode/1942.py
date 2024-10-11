from typing import List, Tuple
import heapq


class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        n = len(times)
        target_data = times[targetFriend]
        times.sort()
        chairs: List[int] = list(range(n))
        heapq.heapify(chairs)
        leaving_data: List[Tuple[int, int]] = []

        for arrival_time, leaving_time in times:
            while leaving_data and leaving_data[0][0] <= arrival_time:
                _, vacating_chair = heapq.heappop(leaving_data)
                heapq.heappush(chairs, vacating_chair)
            req_chair = heapq.heappop(chairs)
            heapq.heappush(leaving_data, (leaving_time, req_chair))
            if [arrival_time, leaving_time] == target_data:
                return req_chair


def main():
    obj = Solution()

    l1 = [[1, 4], [2, 3], [4, 6]]
    l1 = [[3, 10], [1, 5], [2, 6]]

    print(obj.smallestChair(l1, 0))


if __name__ == "__main__":
    main()
