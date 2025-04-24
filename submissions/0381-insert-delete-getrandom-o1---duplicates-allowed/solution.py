class RandomizedCollection:

    def __init__(self):
        self.s = SortedList()
        

    def insert(self, val: int) -> bool:
        ret = val not in self.s
        self.s.add(val)
        return ret

    def remove(self, val: int) -> bool:
        if val in self.s:
            self.s.remove(val)
            return True
        return False
        

    def getRandom(self) -> int:
        return random.choice(self.s)
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
