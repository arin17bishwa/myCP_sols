class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.running_length: int = 0

    def consec(self, num: int) -> bool:
        if num == self.value:
            self.running_length += 1
        else:
            self.running_length = 0
        return self.running_length >= self.k


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)
