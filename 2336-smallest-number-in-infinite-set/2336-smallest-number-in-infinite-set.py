class SmallestInfiniteSet:

    def __init__(self):
        self.l = []
        for i in range(1, 1001):
            self.l.append(i)

    def popSmallest(self) -> int:
        min1 = min(self.l)
        self.l.remove(min1)
        return min1

    def addBack(self, num: int) -> None:
        if num not in self.l:
            self.l.append(num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)