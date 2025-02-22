from typing import Dict, Optional


class Node:
    def __init__(
        self, val=0, prev: Optional["Node"] = None, nxt: Optional["Node"] = None
    ):
        self.val: int = val
        self.prev: Optional["Node"] = prev
        self.nxt: Optional["Node"] = nxt

    def __repr__(self):
        return f"{self.val}<->{self.nxt}"


class RandomizedSet:

    def __init__(self):
        self.elements: Dict[int, Node] = {}

        self.head = Node(-1)
        self.tail = self.head
        self.curr_ptr: Optional[Node] = None

    def insert(self, val: int) -> bool:
        if val in self.elements:
            return False
        node = Node(val)

        node.prev = self.tail
        self.tail.nxt = node
        self.tail = self.tail.nxt
        self.elements[val] = node
        if not self.curr_ptr:
            self.curr_ptr = self.head.nxt

        return True

    def remove(self, val: int) -> bool:
        if val not in self.elements:
            return False
        node = self.elements.pop(val)
        prev_ptr = node.prev
        nxt_ptr = node.nxt

        node.prev.nxt = nxt_ptr
        if nxt_ptr:
            node.nxt.prev = prev_ptr

        if self.curr_ptr == node:
            if nxt_ptr:
                self.curr_ptr = nxt_ptr
            else:
                self.curr_ptr = self.head.nxt

        if self.tail == node:
            self.tail = node.prev
        del node
        return True

    def getRandom(self) -> int:
        val = self.curr_ptr.val
        if self.curr_ptr.nxt:
            self.curr_ptr = self.curr_ptr.nxt
        else:
            self.curr_ptr = self.head.nxt
        return val


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()


def main():
    obj = RandomizedSet()

    obj.insert(0)
    print(obj.head, obj.elements, obj.curr_ptr)

    obj.remove(0)
    print(obj.head, obj.elements, obj.curr_ptr)

    obj.insert(-1)
    print(obj.head, obj.elements, obj.curr_ptr)

    obj.remove(0)

    print(obj.head)
    print(obj.curr_ptr)
    print(obj.elements)


if __name__ == "__main__":
    main()
