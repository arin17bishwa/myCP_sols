class Bitset:

    def __init__(self, size: int):
        self.arr:list[int]=[0]*size
        self.flipped:list[int]=[1]*size
        self.size=size
        self.set_count:int=0

    def fix(self, idx: int) -> None:
        self.set_count+=1 if  self.arr[idx]==0 else 0
        self.arr[idx]=1
        self.flipped[idx]=0

    def unfix(self, idx: int) -> None:
        self.set_count-=1 if self.arr[idx] else 0
        self.arr[idx]=0
        self.flipped[idx]=1

    def flip(self) -> None:
        self.flipped, self.arr=self.arr, self.flipped
        self.set_count=self.size-self.set_count

    def all(self) -> bool:
        return self.set_count==self.size


    def one(self) -> bool:
        return self.set_count>0


    def count(self) -> int:
        return self.set_count


    def toString(self) -> str:
        return ''.join(map(str, self.arr))



# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()