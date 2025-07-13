class ProductOfNumbers:

    def __init__(self):
        self.prefix_product: list[int] = [1]
        self.current_size: int = 0
        self.last_zero_idx = -1

    def add(self, num: int) -> None:
        self.current_size += 1
        if not self.prefix_product:
            self.prefix_product.append(num)
            return
        if num == 0:
            self.last_zero_idx = self.current_size - 1
            self.prefix_product.append(1)
        else:
            self.prefix_product.append(num * self.prefix_product[-1])

    def getProduct(self, k: int) -> int:
        if self.last_zero_idx >= self.current_size - k:
            return 0
        return self.prefix_product[-1] // self.prefix_product[-k - 1]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)


def main():
    obj = ProductOfNumbers()

    obj.add(1)
    print(obj.getProduct(1))

    for i in [3, 0, 2, 5, 4]:
        obj.add(i)

    print(obj.prefix_product)

    for i in [2, 3, 4]:
        print(obj.getProduct(i))

    obj.add(8)

    print(obj.getProduct(2))


if __name__ == "__main__":
    main()
