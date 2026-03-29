class MyHashMap:

    def __init__(self):
        self.p = 8
        self.m = 1 << self.p
        self.arr: list[list[tuple[int, int]]] = [[] for _ in range(self.m)]

    def put(self, key: int, value: int) -> None:
        key_idx, idx = self.get_idx(key)
        if idx == -1:
            self.arr[key_idx].append((key, value))
        else:
            self.arr[key_idx][idx] = (key, value)

    def get(self, key: int) -> int:
        key_idx, idx = self.get_idx(key)
        if idx == -1:
            return -1
        return self.arr[key_idx][idx][1]

    def remove(self, key: int) -> None:
        key_idx, idx = self.get_idx(key)
        if idx == -1:
            return
        self.arr[key_idx].pop(idx)

    def get_idx(self, key: int) -> tuple[int, int]:
        key_idx = self._get_key_idx(key)
        for idx, (k, v) in enumerate(self.arr[key_idx]):
            if k == key:
                return key_idx, idx
        return key_idx, -1

    def _get_key_idx(self, key: int) -> int:
        key_hash = self._hash(key)
        return key_hash & self.m - 1

    @staticmethod
    def _hash(key) -> int:
        return ((key * 1031237) & (1 << 20) - 1) >> 5


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
