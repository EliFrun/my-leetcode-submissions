class SORTracker:

    def __init__(self):
        self.s = SortedList()
        self.i = 0
        

    def add(self, name: str, score: int) -> None:
        self.s.add((-score, name))
        

    def get(self) -> str:
        ret = self.s[self.i]
        self.i += 1
        return ret[1]
        


# Your SORTracker object will be instantiated and called as such:
# obj = SORTracker()
# obj.add(name,score)
# param_2 = obj.get()
