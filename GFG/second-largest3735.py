class Solution:
    def getSecondLargest(self, arr: list[int]) -> int:
        largest = second_largest = arr[0]

        for ele in arr:
            if largest == second_largest and ele != largest:
                largest, second_largest = max(largest, ele), min(largest, ele)
            elif ele > largest:
                largest, second_largest = ele, largest
            elif largest > ele > second_largest:
                second_largest = ele
        return -1 if largest == second_largest else second_largest
