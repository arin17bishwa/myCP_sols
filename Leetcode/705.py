class MyHashSet:

    def __init__(self):
        self.m = 10**5
        self.arr: list[list[int]] = [[] for _ in range(self.m)]

    def add(self, key: int) -> None:
        key_idx = self._get_key_idx(key)
        if key not in self.arr[key_idx]:
            self.arr[key_idx].append(key)

    def remove(self, key: int) -> None:
        key_idx = self._get_key_idx(key)
        if key in self.arr[key_idx]:
            self.arr[key_idx].remove(key)

    def contains(self, key: int) -> bool:
        return key in self.arr[self._get_key_idx(key)]

    def _get_key_idx(self, key: int) -> int:
        key_hash = self._hash(key)
        return key_hash % self.m

    @staticmethod
    def _hash(val) -> int:
        return hash(val)


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
