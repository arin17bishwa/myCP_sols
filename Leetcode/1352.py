from typing import List


class ProductOfNumbers:

    def __init__(self):
        self.prefix_prod: List[int] = [1]
        self.running_size: int = 0

    def add(self, num: int) -> None:
        if num == 0:
            self.prefix_prod = [1]
        else:
            self.prefix_prod.append(num * self.prefix_prod[-1])

    def getProduct(self, k: int) -> int:
        if k > len(self.prefix_prod) - 1:
            return 0
        return self.prefix_prod[-1] // self.prefix_prod[len(self.prefix_prod) - k - 1]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
