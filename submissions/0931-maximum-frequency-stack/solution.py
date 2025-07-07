class FreqStack:

    def __init__(self):
        self.l = SortedList([])
        self.idxs = {}
        self.t = 0

    def push(self, val: int) -> None:
        count, times, = 0, []
        if val in self.idxs:
            count, times, _ = self.l.pop(self.l.index(self.idxs[val]))

        times = [self.t] + times
        count += 1
        self.l.add((count, times, val))
        self.idxs[val] = (count, times, val)
        self.t += 1
        
    def pop(self) -> int:
        count, times, val = self.l.pop()
        count -= 1
        times.pop(0)
        if count != 0:
            self.l.add((count, times, val))
            self.idxs[val] = (count, times, val)
        else:
            self.idxs.pop(val)
        return val
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
