class RecentCounter:

    def __init__(self):
        self.lis = SortedList([])
        

    def ping(self, t: int) -> int:
        self.lis.add(t)
        return self.lis.bisect_right(t) - self.lis.bisect_left(t - 3000)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
