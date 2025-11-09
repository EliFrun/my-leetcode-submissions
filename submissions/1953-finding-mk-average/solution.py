class MKAverage:

    def __init__(self, m: int, k: int):
        self.q = deque()
        self.m = m
        self.k = k
        self.s = 0
        self.bottom_k = SortedList()
        self.top_k = SortedList()
        self.average_list = SortedList()
        

    def addElement(self, num: int) -> None:
        self.q.append(num)
        if len(self.q) > self.m:
            v = self.q.popleft()
            if v in self.top_k:
                self.top_k.remove(v)
            elif v in self.average_list:
                self.average_list.remove(v)
                self.s -= v
            else:
                self.bottom_k.remove(v)
        
        self.bottom_k.add(num)
        while len(self.bottom_k) > self.k:
            v = self.bottom_k.pop()
            self.s += v
            self.average_list.add(v)
        while self.bottom_k and self.average_list and self.bottom_k[-1] > self.average_list[0]:
            v,w = self.bottom_k.pop(), self.average_list.pop(0)
            self.s -= w
            self.s += v
            self.bottom_k.add(w)
            self.average_list.add(v)

        while len(self.average_list) > self.m - 2 * self.k:
            v = self.average_list.pop()
            self.s -= v
            self.top_k.add(v)

        while self.average_list and self.top_k and self.average_list[-1] > self.top_k[0]:
            v, w = self.average_list.pop(), self.top_k.pop(0)
            self.s -= v
            self.s += w
            self.average_list.add(w)
            self.top_k.add(v)

        

    def calculateMKAverage(self) -> int:
        #print(self.q, self.bottom_k, self.average_list, self.top_k, self.s)
        if len(self.q) < self.m :
            return -1
        return self.s // len(self.average_list)
        


# Your MKAverage object will be instantiated and called as such:
# obj = MKAverage(m, k)
# obj.addElement(num)
# param_2 = obj.calculateMKAverage()
