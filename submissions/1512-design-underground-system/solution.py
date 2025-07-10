class UndergroundSystem:

    def __init__(self):
        self.trips = {}
        self.times = defaultdict(lambda: [0, 0])
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.trips[id] = [stationName, t]
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        l = self.times[(self.trips[id][0], stationName)]
        l[0] += 1
        l[1] += t - self.trips[id][1]
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        c, t = self.times[(startStation, endStation)]
        return t/c if c > 0 else -1


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
