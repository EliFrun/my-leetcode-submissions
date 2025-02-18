class MedianFinder:

    def __init__(self):
        self.lis = SortedList()
        

    def addNum(self, num: int) -> None:
        self.lis.add(num)

    def findMedian(self) -> float:
        n = len(self.lis)
        if len(self.lis) % 2 == 0:
            return (self.lis[n//2 - 1] + self.lis[n//2]) / 2

        return float(self.lis[n//2])


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
