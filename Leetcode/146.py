from typing import Optional


class DLL:
    def __init__(
        self,
        val: int,
        key: int,
        prev: Optional["DLL"] = None,
        nxt: Optional["DLL"] = None,
    ):
        self.val: int = val
        self.key: int = key

        self.nxt: Optional[DLL] = nxt
        self.prev: Optional[DLL] = prev

    def __str__(self):
        return f"({self.key},{self.val})-> {self.nxt}"

    def __repr__(self):
        return self.__str__()


class LRUCache:

    def __init__(self, capacity: int):
        self.head = DLL(-1, -1)
        self.tail = DLL(-1, -1, self.head)
        self.head.nxt = self.tail

        self.max_capacity = capacity
        self.kv: dict[int, DLL] = {}

    def get(self, key: int) -> int:
        dll = self.kv.get(key)
        self.move_to_front(dll)
        return -1 if dll is None else dll.val

    def put(self, key: int, value: int) -> None:
        existing_dll = self.kv.get(key)
        if existing_dll:
            existing_dll.val = value
            self.move_to_front(existing_dll)
            return
        dll = DLL(value, key, self.head, self.head.nxt)

        if len(self.kv) < self.max_capacity:
            self.kv[key] = dll
        else:
            dll = self.tail.prev
            del self.kv[dll.key]
            dll.key = key
            dll.val = value
            self.kv[key] = dll
        self.move_to_front(dll)

    def move_to_front(self, dll: Optional[DLL]):
        if not dll:
            return

        dll.prev.nxt = dll.nxt
        dll.nxt.prev = dll.prev

        dll.nxt = self.head.nxt
        dll.prev = self.head

        self.head.nxt.prev = dll
        self.head.nxt = dll


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
