class MyHashSet:

    def __init__(self):
        self.p = 10
        self.m = 1 << self.p
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
        return key_hash & self.m - 1

    @staticmethod
    def _hash(key) -> int:
        return ((key * 1031237) & (1 << 20) - 1) >> 5


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
