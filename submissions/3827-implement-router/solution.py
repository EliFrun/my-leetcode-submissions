class Router:

    def __init__(self, memoryLimit: int):
        self.q = SortedList()
        self.d = defaultdict(SortedList)
        self.m = memoryLimit
        self.v = 0
        

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        if (timestamp, source) in self.d[destination]:
            return False
        self.v += 1
        if len(self.q) == self.m:
            v1,_,v2,v3 = self.q.pop(0)
            self.d[v3].remove((v1,v2))
        self.q.add((timestamp, self.v, source, destination))
        self.d[destination].add((timestamp, source))
        return True
        

    def forwardPacket(self) -> List[int]:
        if not self.q:
            return []
        v1,_,v2,v3 = self.q.pop(0)
        self.d[v3].remove((v1,v2))
        return([v2,v3,v1])
        

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        return self.d[destination].bisect_left((endTime, float(inf))) - self.d[destination].bisect_left((startTime, -1))
        
        


# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)
