class FrequencyTracker:

    def __init__(self):
        self.d = defaultdict(int)
        self.s = defaultdict(int)
        

    def add(self, number: int) -> None:
        v = self.d[number]
        self.d[number] += 1
        self.s[v] -= 1
        self.s[v + 1] += 1
        

    def deleteOne(self, number: int) -> None:
        v = self.d[number]
        self.d[number] = max(self.d[number] - 1, 0)
        self.s[v] = max(self.s[v] - 1, 0)
        if v - 1 > 0:
            self.s[v - 1] += 1
        

    def hasFrequency(self, frequency: int) -> bool:
        return self.s[frequency] > 0
        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)
