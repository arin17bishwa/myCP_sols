from typing import List


class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        total_wait_time: int = 0
        if not customers:
            return 0
        curr_time: int = customers[0][0]
        for customer in customers:
            final_time = max(curr_time, customer[0]) + customer[1]
            total_wait_time += final_time - customer[0]
            curr_time = final_time
        return total_wait_time / len(customers)
