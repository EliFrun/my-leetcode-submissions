class SmallestInfiniteSet:

    def __init__(self):
        self.q = []
        self.curr = 1
        

    def popSmallest(self) -> int:
        if not self.q:
            ret = self.curr
            self.curr += 1
            return ret
        
        ret = heapq.heappop(self.q)
        while self.q and ret == self.q[0]:
            heapq.heappop(self.q)
        return ret

        

    def addBack(self, num: int) -> None:
        if num < self.curr:
            heapq.heappush(self.q, num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
