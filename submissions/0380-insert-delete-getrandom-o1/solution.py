class RandomizedSet:

    def __init__(self):
        self.l = []
        self.value_valid = {}
        

    def insert(self, val: int) -> bool:
        if val in self.value_valid:
            if self.value_valid[val][0] == True:
                return False
            self.value_valid[val][0] = True
        else:
            self.l.append(val)
            self.value_valid[val] = [True, len(self.l) - 1]
        return True


    def remove(self, val: int) -> bool:
        if val not in self.value_valid:
            return False
        elif not self.value_valid[val][0]:
            return False
        self.value_valid[val][0] = False
        return True
        

    def getRandom(self) -> int:
        v = random.choice(self.l)
        while self.value_valid[v][0] == False:
            v = random.choice(self.l)
        return v


        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
